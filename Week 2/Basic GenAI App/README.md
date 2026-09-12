# GenAI Restricted Trivia App 🧠

A specialized interactive web application built with [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/) that delivers fascinating trivia about **Science** and **Sports** for events, history, and discoveries up to the year **2021**.

## Features

- **Topic Restriction Guardrails:** Strictly restricts answers to Science and Sports domains. Any unrelated topics (e.g., movies, pop culture, cooking) trigger a polite restriction message.
- **Temporal Constraint:** Ensures all historical facts and trivia adhere strictly to a cut-off year of 2021, avoiding post-2021 milestones.
- **Interactive UI:** Clean and simple Streamlit web interface for easy topic input and instant feedback.

## Tech Stack

- **Python 3.8+**
- **Streamlit** (Frontend UI)
- **LangChain** (LLM Orchestration & Prompt Management)
- **OpenAI GPT-3.5 Turbo** (Language Model)
- **python-dotenv** (Environment Variable Management)

---

## Installation & Setup

### 1. Clone the Repository
Clone this repository or save the script as `main.py` in your local directory.

### 2. Install Dependencies
Make sure you have Python installed, then install the required packages using pip:

```bash
pip install streamlit langchain langchain-openai langchain-core python-dotenv openai
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory of your project and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Running the Application

To run the Streamlit app locally, execute the following command in your terminal:

```bash
streamlit run main.py
```

This will launch a local web server and open the app automatically in your default web browser (typically at `http://localhost:8501`).

---

## Usage Guide

1. Open the application in your browser.
2. Enter a **Science** or **Sports** topic (e.g., *FIFA*, *Quantum Physics*, *Space Exploration*, *Basketball*) into the text box.
3. Click the **"Get Trivia!"** button.
4. View the verified, historically accurate trivia generated within the 2021 cutoff window.
