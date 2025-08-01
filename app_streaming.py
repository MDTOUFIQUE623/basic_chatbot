import streamlit as st
import google.generativeai as genai
import os
import time
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
            # Show thinking indicator while waiting for first token
            thinking_placeholder = st.empty()
            thinking_placeholder.markdown("Thinking...")
            
            # Use write_stream for smoother streaming
            def response_generator():
                first_chunk = True
                for chunk in get_gemini_response_stream(prompt):
                    if first_chunk:
                        thinking_placeholder.empty()  # Remove thinking indicator
                        first_chunk = False
                    yield chunk
                    time.sleep(0.01)  # Small delay for smoother animation
            
            # Stream the response
            full_response = st.write_stream(response_generator)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()