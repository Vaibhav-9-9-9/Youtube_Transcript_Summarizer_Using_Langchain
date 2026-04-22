import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = st.get_secrets["GEMINI_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite'
)
