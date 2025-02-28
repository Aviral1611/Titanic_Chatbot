import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="Titanic Chatbot", page_icon="🚢", layout="wide")

# Title and description
st.title("Titanic Chatbot 🚢")
st.markdown("Ask questions about the Titanic dataset in plain English, and get text answers!")

# Backend API URL
BACKEND_URL = "http://127.0.0.1:8000/query"

# Input field for user question
question = st.text_input("Enter your question:", placeholder="e.g., What percentage of passengers were male on the Titanic?")

# Button to submit query
if st.button("Ask"):
    if question:
        try:
            # Make GET request to backend
            response = requests.get(BACKEND_URL, params={"question": question})
            response.raise_for_status()  # Check for HTTP errors
            
            # Parse JSON response
            data = response.json()
            answer = data.get("text", "No answer received.")
            
            # Display the answer
            st.subheader("Answer:")
            st.write(answer)
        
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {str(e)}")
    else:
        st.warning("Please enter a question!")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit and FastAPI | Powered by Gemini API")