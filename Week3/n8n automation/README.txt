n8n Automated Student Data Pipeline & Routing Workflow
This n8n workflow automates the ingestion, AI-powered extraction, cleaning, validation, and multi-conditional routing of student data records (e.g., from CSV submissions or forms) into structured categories.

Workflow Overview
[On Form Submission] 
       ↓
[Extract from File (CSV)] 
       ↓
[Basic LLM Chain (OpenAI)] 
       ↓
[Code in JavaScript (Clean & Validate)] 
       ↓
[Switch (Location Filter: Chennai vs Other)]
       ├── (Chennai) → [Switch1 (Email Validity)]
       │                ├── (Valid Email)    → Chennai Valid Output
       │                └── (Invalid Email)  → Chennai Invalid Output
       │
       └── (Other)   → [Switch2 (Email Validity)]
                        ├── (Valid Email)    → Other Valid Output
                        └── (Invalid Email)  → Other Invalid Output
Detailed Step-by-Step Architecture
On Form Submission (n8n Trigger): Initiates the workflow execution when a new student form or file payload is submitted.

Extract from File (Extract from File): Parses the incoming raw data (e.g., a CSV file containing student records) into structured items.

Basic LLM Chain & OpenAI Chat Model (Basic LLM Chain): Passes the data through an LLM to parse and structure raw records into standard JSON objects.

Code in JavaScript (Code in JavaScript):

Handles text-wrapped JSON outputs from the AI node.

Cleans and formats fields (Name, Phone, Enrolled_Date).

Validates email addresses, normalizing valid ones and setting invalid ones to null with Email_Valid: false.

Normalizes city names and catches common spelling variants (e.g., variations of Chennai).

Appends a unified Category tag string for precise conditional routing.

Switch Node (Switch - Location Filter): Evaluates the student's City property to split records into Chennai-based entries versus all other cities.

Secondary Switch Nodes (Switch1 & Switch2 - Email Validation): Further splits the location branches based on email health (Email_Valid: true vs false), resulting in four clean sub-routes:

Chennai + Valid Email

Chennai + Invalid Email

Other Cities + Valid Email

Other Cities + Invalid Email

JavaScript Code Snippet Used in the Cleaning Node
JavaScript
// Loop through all incoming items from the n8n execution context
for (let item of $input.all()) {
  // Handle cases where the AI node returns the JSON as a string inside a 'text' property, or as a direct JSON object
  let rawData = item.json.text || item.json;
  let record = typeof rawData === 'string' ? JSON.parse(rawData) : rawData;

  // Clean and validate the Email field
  let email = record.Email;
  if (!email || email === 'INVALID_EMAIL' || !email.includes('@')) {
    record.Email = null;           // Clear invalid or missing emails
    record.Email_Valid = false;    // Flag email as invalid
  } else {
    record.Email_Valid = true;     // Flag email as valid
    record.Email = email.trim().toLowerCase(); // Normalize email format
  }

  // Trim whitespace from Name and ensure Phone is formatted safely as a string
  if (record.Name) record.Name = record.Name.trim();
  if (record.Phone) record.Phone = String(record.Phone).trim();

  // Standardize the Date format to a clean YYYY-MM-DD string
  if (record.Enrolled_Date) {
    record.Enrolled_Date = new Date(record.Enrolled_Date).toISOString().split('T')[0];
  }

  // Clean the City field and handle common typos or variations
  let cityRaw = record.City ? record.City.trim().toLowerCase() : 'other';
  let isChennai = ['chennai', 'chenai', 'chennnai'].includes(cityRaw);
  let city = isChennai ? 'Chennai' : record.City.trim();
  record.City = city;

  // Determine the routing category based on Location and Email Validity
  if (isChennai && record.Email_Valid) {
    record.Category = 'chennai_valid_email';
  } else if (isChennai && !record.Email_Valid) {
    record.Category = 'chennai_invalid_email';
  } else if (!isChennai && record.Email_Valid) {
    record.Category = 'other_valid_email';
  } else {
    record.Category = 'other_invalid_email';
  }

  // Update the n8n item json with the processed record object
  item.json = record;
}

// Return all modified items back into the n8n workflow pipeline
return $input.all();
Setup Instructions
Import the workflow JSON file into your n8n instance.

Configure your OpenAI Chat Model credential inside the Basic LLM Chain node.

Update the file ingestion node (Extract from File) to match your target file path or form upload configuration.

Replace or attach independent output nodes (such as individual Google Sheets, Airtable, or Write-to-File nodes) to the four respective branches coming out of Switch1 and Switch2 to store segregated records independently.
