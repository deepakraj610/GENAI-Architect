import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

# Configure the Streamlit page layout
st.title("🧠 GenAI Restricted Trivia App")
st.write("Discover science and sports trivia for events up to the year 2021.")

# Initialize the LangChain components
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

# Updated prompt to handle topic validation separately from the year filter
prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are a helpful trivia expert. Your scope is strictly limited to Science or Sports topics.\n\n"
     "Guidelines:\n"
     "1. If the topic is completely unrelated to Science or Sports (e.g., movies, pop culture, cooking), you must respond with: 'I can only provide science or sports trivia up to the year 2021.'\n"
     "2. If the topic IS about Science or Sports (like FIFA, football, physics, space, etc.), provide a fascinating, accurate fact. Ensure the fact pertains to history, events, or discoveries from the year 2021 or earlier, avoiding any post-2021 milestones."
    ),
    ("human", "Give me an interesting fact about {topic}."),
])

chain = prompt | llm | StrOutputParser()

# UI Inputs
topic = st.text_input("Enter a science or sports topic:", "FIFA")

# Action Button
if st.button("Get Trivia!"):
  if topic:
    with st.spinner("Verifying constraints and gathering trivia..."):
      response = chain.invoke({"topic": topic})
      st.success(response)
  else:
    st.warning("Please enter a topic first.")