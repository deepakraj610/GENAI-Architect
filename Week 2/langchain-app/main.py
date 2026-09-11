import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.")
        return

    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = "Tell me a fun fact about Tamil Nadu in 50 words."

    response = model.invoke(prompt)

    print("\nInput:")
    print(prompt)

    print("\nOutput:")
    print(response.content)


if __name__ == "__main__":
    main()