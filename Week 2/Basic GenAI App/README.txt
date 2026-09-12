# ⏳ Time Capsule Trivia Master

An interactive, constraint-aware GenAI application built with Python, LangChain, and Streamlit. This app uncovers fascinating historical facts and trivia specifically for **Science** and **Sports** topics up to the year **2021**, using strict prompt guardrails to filter out off-topic queries and post-2021 events.

---

## 🚀 Features

- **LangChain Integration:** Utilizes prompt templates, OpenAI chat models (`gpt-3.5-turbo`), and string output parsers for clean generation.
- **Strict Guardrails & Constraints:** Configured with robust system prompts to restrict scope exclusively to Science and Sports, capping historical context at 2021.
- **Creative Streamlit UI:** Features a polished layout with domain selection, dynamic status spinners, and a persistent discovery log session history (`st.session_state`).
- **Environment Security:** Securely loads API keys using `python-dotenv`.

---

## 🛠️ Prerequisites & Installation

Follow these step-by-step instructions to set up and run the application locally.

### 1. Clone or Open Project Folder
Navigate to your project directory in your terminal:
```bash
cd C:\Users\DELL\MyfirstGenAIapp\MyFirstGenAIApp
```

### 2. Create and Activate a Virtual Environment
```bash
# Create the virtual environment
python -m venv MyFirstGenAIApp

# Activate it (PowerShell)
.\MyFirstGenAIApp\Scripts\Activate.ps1
```
*(Note: If you encounter script execution permission errors in PowerShell, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` first.)*

### 3. Install Dependencies
Install the required Python packages inside your active virtual environment:
```bash
pip install streamlit langchain langchain-openai python-dotenv
```

---

## ⚙️ Configuration

1. Create a file named `.env` in your root project folder.
2. Add your OpenAI API key inside the file:
```env
OPENAI_API_KEY="your-actual-openai-api-key-here"
```

---

## 🚀 Running the Application

1. Ensure your virtual environment is active and your `app.py` script is saved in the directory.
2. Launch the Streamlit application:
```bash
streamlit run app.py
```
3. Streamlit will automatically open a local web browser window (typically `http://localhost:8501`) displaying your Time Capsule Trivia app!

---

## 📂 Project Structure

```text
MyfirstGenAIapp/
│
├── MyFirstGenAIApp/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── app.py             # Streamlit application code
│   └── main.py            # CLI/terminal version of the GenAI app
│
├── .env                   # Environment variables (API keys)
└── README.md              # Project documentation
```

---

## 💡 How It Works

1. **User Input:** Selects a domain (`Science` or `Sports`) and enters a specific query topic (e.g., `Quantum Mechanics`, `FIFA World Cup`).
2. **Constraint Check:** The LangChain model evaluates the input against strict negative and positive constraints defined in the system prompt.
3. **Generation:** If valid and within the 2021 historical threshold, a verified trivia fact is returned. Otherwise, a polite boundary message is displayed.
4. **History Log:** Past searches are stored in Streamlit's session state and displayed in a neat chronological discovery card log.
