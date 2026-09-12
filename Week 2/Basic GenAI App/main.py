import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

# Configure the Streamlit page layout
st.title("🧠 GenAI Facts & Trivia App")
st.write("Discover surprising facts and hidden trivia about any topic.")

# Initialize the LangChain components
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert trivia master and historian. Share one fascinating, lesser-known, and accurate fact about the given topic."),
    ("human", "Give me an interesting fact about {topic}."),
])
chain = prompt | llm | StrOutputParser()

# UI Inputs
topic = st.text_input("Enter a topic:", "Cricket")

# Action Button
if st.button("Get Trivia!"):
  if topic:
    with st.spinner("Digging up fascinating facts..."):
      response = chain.invoke({"topic": topic})
      st.success(response)
  else:
    st.warning("Please enter a topic first.")