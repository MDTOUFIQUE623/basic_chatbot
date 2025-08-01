import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(question):
    """Get response from Gemini AI"""
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Page configuration
    st.set_page_config(
        page_title="AI Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    
    
    # Header
    st.title("🤖 AI Chatbot")
    st.markdown("---")
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    

if __name__ == "__main__":
    main()
