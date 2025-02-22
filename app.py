import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

import streamlit as st

st.title("Relief Bot")
st.write("This is a test deployment for my chatbot.")



# Load API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="💬")

st.title("💬 Chatbot with Gemini API")
st.write("Ask me anything!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    # Get response from Gemini API
    response = model.generate_content(user_input).text
    st.session_state.messages.append({"role": "bot", "text": response})

    # Display response
    with st.chat_message("bot"):
        st.markdown(response)
