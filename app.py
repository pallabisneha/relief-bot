import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("🤖 Gemini Chatbot")
st.write("Powered by Google's Gemini API")

# User input
user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input:
        response = get_gemini_response(user_input)
        st.write("💬 Chatbot:", response)
    else:
        st.warning("Please enter a message!")
