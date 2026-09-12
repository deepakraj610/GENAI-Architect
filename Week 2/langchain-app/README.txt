# LangChain OpenAI Quickstart

A simple Python script demonstrating how to use LangChain with the OpenAI API (`gpt-4o-mini`) to generate responses.

## Prerequisites

- Python 3.8+
- An OpenAI API Key

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies:

```bash
pip install langchain-openai python-dotenv
```

3. Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the script using Python:

```bash
python main.py
```

## Code Overview

The script initializes a `ChatOpenAI` model using the `gpt-4o-mini` engine with a deterministic temperature (`0`), sends a prompt asking for a fun fact about Tamil Nadu, and prints the result to the console.
