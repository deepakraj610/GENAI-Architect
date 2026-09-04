import pyautogui
import pyperclip
import time
from datetime import datetime
from pathlib import Path


# ============================================================
# SETTINGS
# ============================================================

# Folder where reports will be saved
REPORT_FOLDER = (Path.home() / "Documents" / "daily-report-bot" / "reports")
#REPORT_FOLDER = r"C:\Users\DELL\Documents\daily-report-bot\reports"

#REPORT_FOLDER =  Path.home() / "daily-report-bot" / "reports"

# Create folder if it doesn't exist
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# Today's date/time
now = datetime.now()

#date_string = now.strftime("%Y-%m-%d")
datetime_string = now.strftime("%Y-%m-%d %H%M%S")

excel_filename = f"daily_report_{datetime_string}.xlsx"
screenshot_filename = REPORT_FOLDER / f"daily_report_{datetime_string}.png"


# ============================================================
# SAFETY SETTINGS
# ============================================================

# Move mouse to the top-left corner to immediately stop
# the program if something goes wrong.
pyautogui.FAILSAFE = True

# Small delay between PyAutoGUI actions
pyautogui.PAUSE = 0.5


# ============================================================
# STEP 1 - OPEN CHROME
# ============================================================

print("Step 1: Opening Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)


# ============================================================
# STEP 2 - OPEN WEATHER WEBSITE
# ============================================================

print("Step 2: Opening weather website...")

pyautogui.hotkey("ctrl", "l")

pyautogui.write(
    "https://www.google.com/search?q=Chennai+weather"
)

pyautogui.press("enter")

time.sleep(5)


# ============================================================
# STEP 3 - COPY INFORMATION FROM THE PAGE
# ============================================================

print("Step 3: Copying weather information...")

# For this learning example, we use Ctrl+A / Ctrl+C.
#
# This copies the visible webpage text into the clipboard.
#
# IMPORTANT:
# Ctrl+A may select the entire webpage, not just the temperature.
# We will extract the useful information from the clipboard below.

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

time.sleep(1)

page_text = pyperclip.paste()

print("\nCopied webpage text:")
print(page_text[:1000])


# ============================================================
# STEP 4 - EXTRACT A SIMPLE PIECE OF INFORMATION
# ============================================================

print("\nStep 4: Extracting weather information...")

# This is intentionally simple because we are learning
# PyAutoGUI first.
#
# Google normally displays something similar to:
#
# 29°C
# Sunny
#
# We look for a temperature containing °C.

weather_value = "Weather information not found"

lines = page_text.splitlines()

for line in lines:

    line = line.strip()

    if "°C" in line:

        weather_value = line

        break


print("Fetched data:", weather_value)


# ============================================================
# STEP 5 - CREATE A COMMENT
# ============================================================

print("Step 5: Creating comment...")

comment = "Good for outdoor activities"


# ============================================================
# STEP 6 - OPEN MICROSOFT EXCEL
# ============================================================

print("Step 6: Opening Microsoft Excel...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("excel")
pyautogui.press("enter")

time.sleep(5)


# ============================================================
# STEP 7 - CREATE NEW WORKBOOK
# ============================================================

print("Step 7: Creating new Excel workbook...")

# Depending on your Excel version, the start screen may appear.
#
# Ctrl+N creates a new workbook.

pyautogui.hotkey("ctrl", "n")

time.sleep(3)


# ============================================================
# STEP 8 - ENTER HEADERS
# ============================================================

print("Step 8: Entering headers...")

# We enter three columns:
#
# A1 = Date & Time
# B1 = Fetched Data
# C1 = Comment

pyautogui.write("Date & Time")
pyautogui.press("tab")

pyautogui.write("Fetched Data")
pyautogui.press("tab")

pyautogui.write("Comment")

pyautogui.press("enter")


# ============================================================
# STEP 9 - ENTER DATA
# ============================================================

print("Step 9: Entering report data...")

# Date/time

pyautogui.write(datetime_string)

pyautogui.press("tab")

# Weather data

pyautogui.write(weather_value)

pyautogui.press("tab")

# Comment

pyautogui.write(comment)

print("Data entered successfully.")

pyautogui.press("enter")

# ============================================================
# STEP 10 - SAVE EXCEL FILE
# ============================================================

print("Step 10: Saving Excel file...")

pyautogui.hotkey("ctrl", "s")

time.sleep(3)


# Type the complete filename

pyautogui.hotkey("ctrl", "a")

pyautogui.write(str(excel_filename))

pyautogui.press("enter")

time.sleep(4)


# Handle possible Excel confirmation dialogs

pyautogui.press("enter")

time.sleep(2)


print("Excel saved as:")
print(excel_filename)


# ============================================================
# STEP 11 - TAKE SCREENSHOT
# ============================================================

print("Step 11: Taking screenshot...")

# Make sure Excel is visible

pyautogui.hotkey("alt", "tab")
time.sleep(2)

pyautogui.hotkey("ctrl", "r")

time.sleep(2)

# Screenshot entire screen

screenshot = pyautogui.screenshot()

screenshot.save(screenshot_filename)


print("Screenshot saved as:")
print(screenshot_filename)


# ============================================================
# FINISHED
# ============================================================

print("\n===================================")
print(" DAILY REPORT BOT COMPLETED")
print("===================================")

print("Excel file:")
print(excel_filename)

print("\nScreenshot:")
print(screenshot_filename)