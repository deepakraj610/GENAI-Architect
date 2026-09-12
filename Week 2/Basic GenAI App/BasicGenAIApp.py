import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

# Page Configuration for a polished look and title/favicon
st.set_page_config(
    page_title="Time Capsule Trivia",
    page_icon="⏳",
    layout="centered"
)

# Custom styled header using Markdown HTML
st.markdown("""
    <div style='text-align: center;'>
        <h1>⏳ Time Capsule Trivia Master</h1>
        <p style='color: gray;'>Uncover fascinating Science & Sports facts frozen in time (up to the year 2021).</p>
    </div>
    <hr style='margin-bottom: 30px;'>
""", unsafe_allow_html=True)

# Initialize LangChain components
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert historical trivia master. Your scope is strictly limited to Science or Sports topics up to the year 2021.\n\n"
     "Guidelines:\n"
     "1. If the topic is completely unrelated to Science or Sports, or references events after 2021, respond with: 'I can only provide science or sports trivia up to the year 2021.'\n"
     "2. Otherwise, provide a fascinating, accurate fact about the topic from 2021 or earlier."
    ),
    ("human", "Give me an interesting fact about {topic} in the field of {category}."),
])

chain = prompt | llm | StrOutputParser()

# Initialize Session State to keep track of searched trivia
if "history" not in st.session_state:
    st.session_state.history = []

# Creative UI Layout using columns and containers
with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        category = st.selectbox("🎯 Choose Domain", ["Science", "Sports"])
    with col2:
        subtopic = st.text_input("🔍 Specific Topic", "FIFA World Cup")
        
    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        submitted = st.button("✨ Discover", type="primary")
    with col_btn2:
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()

# Handle Discovery Action
if submitted:
    if subtopic:
        with st.spinner("⏳ Traveling back in time..."):
            response = chain.invoke({"topic": subtopic, "category": category})
            # Save to session history (most recent first)
            st.session_state.history.insert(0, {"category": category, "topic": subtopic, "fact": response})
    else:
        st.warning("Please enter a specific topic.")

# Display History in sleek card containers
if st.session_state.history:
    st.markdown("### 📜 Discovery Log")
    for item in st.session_state.history:
        with st.container(border=True):
            st.markdown(f"**[{item['category'].upper()}] {item['topic']}**")
            st.write(item['fact'])
