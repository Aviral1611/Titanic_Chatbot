import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(
    page_title="Titanic Chatbot",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Background and text styling */
    .stApp {
        background: linear-gradient(to bottom right, #e6f0fa, #b3cde0);
        color: #333;
    }
    .stTitle {
        font-family: 'Arial', sans-serif;
        color: #1e3d59;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
    }
    .stMarkdown {
        font-family: 'Arial', sans-serif;
        color: #4a4a4a;
        text-align: center;
    }
    /* Input field styling */
    .stTextInput > div > div > input {
        border: 2px solid #1e3d59;
        border-radius: 8px;
        padding: 10px;
        font-size: 1.1rem;
        background-color: #fff;
        color: #333;
    }
    /* Button styling */
    .stButton > button {
        background-color: #ff6f61;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #e65b50;
    }
    /* Answer box */
    .answer-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-size: 1.2rem;
        color: #333;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1e3d59;
        color: white;
    }
    .css-1d391kg .stMarkdown {
        color: white;
    }
    /* Footer styling */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #1e3d59;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 0.9rem;
    }
    .footer a {
        color: #ff6f61;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: #e65b50;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### About")
    st.markdown("This chatbot answers questions about the Titanic dataset using natural language. Powered by Gemini and built with FastAPI and Streamlit.")
    st.markdown("### Tips")
    st.markdown("- Try: 'What percentage of passengers were male?'")
    st.markdown("- Or: 'What was the average ticket fare?'")

# Title and description
st.title("Titanic Chatbot 🚢")
st.markdown("Ask questions about the Titanic  in plain English and get instant answers!")

# Backend API URL
BACKEND_URL = "http://127.0.0.1:8000/query"

# Input field and button in a centered container
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    question = st.text_input("Enter your question:", placeholder="e.g., What percentage of passengers were male on the Titanic?", label_visibility="collapsed")
    if st.button("Ask"):
        if question:
            try:
                # Make GET request to backend
                response = requests.get(BACKEND_URL, params={"question": question})
                response.raise_for_status()
                
                # Parse JSON response
                data = response.json()
                answer = data.get("text", "No answer received.")
                
                # Display the answer in a styled box
                st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
            
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to backend: {str(e)}")
        else:
            st.warning("Please enter a question!")

# Footer with your name and GitHub link
st.markdown("""
    <div class="footer">
        Made by Aviral Bansal | 
        <a href="https://github.com/Aviral1611" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20" style="vertical-align: middle; margin-left: 5px;">
        </a>
    </div>
""", unsafe_allow_html=True)