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

def get_gemini_response_stream(question):
    """Get streaming response from Gemini AI"""
    try:
        response = model.generate_content(question, stream=True)
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"Error: {str(e)}"

def main():
    # Page configuration
    st.set_page_config(
        page_title="AI Chatbot (Streaming)",
        page_icon="🤖",
        layout="centered"
    )
    
    # Header
    st.title("🤖 AI Chatbot (Streaming)")
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
        
        # Display assistant response with streaming
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            for chunk in get_gemini_response_stream(prompt):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")
            
            # Remove cursor and show final response
            message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()