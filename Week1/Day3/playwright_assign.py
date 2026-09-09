import pandas as pd
import json
import time
import random
from datetime import datetime
from playwright.sync_api import sync_playwright

# File names based on assignment requirements
CONTACTS_FILE = "contacts.xlsx"
DATE_STR = datetime.now().strftime("%Y-%m-%d")
REPORT_JSON = f"whatsapp_report_{DATE_STR}.json"
REPORT_EXCEL = f"whatsapp_report_{DATE_STR}.xlsx"

def random_delay(min_sec=2.0, max_sec=5.0):
    """Adds a human-like random delay between actions to prevent bans."""
    time.sleep(random.uniform(min_sec, max_sec))

def main():
    # 1. Read contacts from Excel
    try:
        contacts_df = pd.read_excel(CONTACTS_FILE)
        print(f"Loaded {len(contacts_df)} contacts from {CONTACTS_FILE}")
    except Exception as e:
        print(f"Failed to load {CONTACTS_FILE}: {e}")
        return

    report_data = []

    with sync_playwright() as p:
        # 2. Launch browser and open WhatsApp Web
        browser = p.chromium.launch_persistent_context(
            user_data_dir="./whatsapp_session",
            headless=False,
            args=['--start-maximized']
        )
        page = browser.new_page()
        
        print("Navigating to WhatsApp Web...")
        page.goto("https://web.whatsapp.com/", timeout=90000)
        
        # ------------------- ROBUST LOGIN CHECK -------------------
        try:
            print("Waiting for WhatsApp to load (this may take a minute if it's syncing)...")
            page.wait_for_selector('canvas, #pane-side', timeout=90000) 
            
            if page.locator('canvas').is_visible():
                print("Login required. Please scan the QR code with your phone...")
                page.wait_for_selector('#pane-side', timeout=120000) 
                print("Successfully logged in!")
            else:
                print("Already logged in. Skipping QR scan and proceeding...")
                
        except Exception as e:
            print("Timeout Error: WhatsApp Web took too long to load or the layout was not recognized.")
            page.screenshot(path="debug_login_error.png")
            print("Saved debug screenshot to 'debug_login_error.png'")
            raise e 
        # -----------------------------------------------------------
            
        random_delay()

        # 3. Iterate through contacts
        for index, row in contacts_df.iterrows():
            name = str(row.get("Name", "")).strip()
            phone = str(row.get("Phone", "")).strip()
            raw_message = str(row.get("Message", "")).strip()
            
            message = raw_message.replace("{name}", name)
            
            contact_status = {
                "Name": name,
                "Phone": phone,
                "Sent_Status": "Failed",
                "Screenshot_Path": "",
                "Extracted_Messages": []
            }

            print(f"\nProcessing contact: {name} ({phone})")

            try:
                page.wait_for_timeout(2000)

                # Clear previous search if any
                cancel_btn = page.locator('button[aria-label="Cancel search"], span[data-icon="x-alt"]').first
                if cancel_btn.is_visible():
                    cancel_btn.click()
                    random_delay(1, 2)

                print("Looking for the search box...")
                
                # ------------------- KITCHEN SINK SEARCH LOCATOR -------------------
                # This covers inputs, contenteditables, titles, labels, and accessibility roles
                search_box = page.locator(
                    '#side input, '
                    '#side [contenteditable="true"], '
                    '[title="Search input textbox"], '
                    '[title="Search or start new chat"], '
                    'button[aria-label="Search or start new chat"]'
                ).first
                
                search_box.wait_for(state="visible", timeout=15000)
                search_box.click()
                
                # Use a keyboard shortcut to select all text and delete it (safer than .clear() for some tags)
                page.keyboard.press("Control+A" if os.name == 'nt' else "Meta+A")
                page.keyboard.press("Backspace")
                
                search_box.fill(phone) 
                # -------------------------------------------------------------------
                
                print(f"Typed phone number: {phone}. Waiting for results...")
                page.wait_for_timeout(3000)
                
                # Select the FIRST result using keyboard navigation 
                print("Opening the chat...")
                page.keyboard.press("ArrowDown") 
                page.wait_for_timeout(1000)
                page.keyboard.press("Enter") 
                random_delay(2, 4)

                print("Typing the message...")
                
                # ------------------- KITCHEN SINK MESSAGE LOCATOR -------------------
                message_box = page.locator(
                    'footer input, '
                    'footer [contenteditable="true"], '
                    'footer [title="Type a message"]'
                ).first 
                
                message_box.wait_for(state="visible", timeout=10000)
                message_box.click()
                message_box.fill(message)
                # --------------------------------------------------------------------
                
                random_delay(1, 3)
                
                page.keyboard.press("Enter")
                print(f"Message sent to {name}.")
                
                # Wait for the message to be sent
                random_delay(3, 5)

                # Take a screenshot
                safe_name = "".join(x for x in name if x.isalnum())
                screenshot_path = f"sent_{safe_name}_{phone}.png"
                page.screenshot(path=screenshot_path)
                contact_status["Screenshot_Path"] = screenshot_path
                contact_status["Sent_Status"] = "Success"
                print(f"Screenshot saved: {screenshot_path}")

                # Smart data extraction: Extract the last 3 messages from the chat
                random_delay(2, 4)
                message_elements = page.locator('div.message-in, div.message-out').element_handles()
                
                extracted = []
                for el in message_elements[-3:]:
                    text_el = el.query_selector('span.selectable-text')
                    if text_el:
                        extracted.append(text_el.inner_text())
                
                contact_status["Extracted_Messages"] = extracted
                print(f"Extracted {len(extracted)} recent messages.")

            except Exception as e:
                print(f"Error processing {name} ({phone}): {str(e)}")
                # Capture the exact moment of failure
                safe_name = "".join(x for x in name if x.isalnum())
                error_shot = f"error_{safe_name}.png"
                page.screenshot(path=error_shot)
                print(f"Saved error screenshot to {error_shot}. Check this image to see what went wrong!")
            
            report_data.append(contact_status)
            random_delay(3, 6) 

        # 4. Generate Reports
        print("\nGenerating reports...")
        
        with open(REPORT_JSON, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)
        
        report_df = pd.DataFrame(report_data)
        report_df['Extracted_Messages'] = report_df['Extracted_Messages'].apply(lambda x: " | ".join(x))
        report_df.to_excel(REPORT_EXCEL, index=False)

        print(f"Reports saved: {REPORT_JSON} and {REPORT_EXCEL}")
        browser.close()

import os # Ensure os is imported for the keyboard shortcut logic
if __name__ == "__main__":
    main()