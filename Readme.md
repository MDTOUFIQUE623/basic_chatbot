# 🤖 AI Chatbot with Google Gemini

A simple and powerful AI chatbot built with **Streamlit** and **Google Gemini AI**. This chatbot can engage in natural conversations, answer questions, and provide intelligent responses using Google's latest AI technology.

## ✨ Features

- **🤖 Smart AI Responses**: Powered by Google's Gemini 2.5 Flash model
- **💬 Real-time Chat Interface**: Modern, responsive chat UI
- **📝 Chat History**: Maintains conversation context throughout your session
- **🎨 Clean Design**: Beautiful, user-friendly interface
- **🔒 Secure**: API key management using environment variables
- **⚡ Fast**: Quick response times with optimized AI model

## 🚀 Quick Start

### Prerequisites

Before you begin, make sure you have:
- **Python 3.8 or higher** installed on your computer
- A **Google AI Studio account** (free) to get your API key
- Basic knowledge of using the command line/terminal

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <your-repository-url>
cd basic_Chatbot

# Or simply download and extract the project folder
```

### Step 2: Set Up Your Environment

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Get Your Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key (it looks like: `AIzaSyC...`)

### Step 4: Configure Your API Key

1. Create a file named `.env` in your project folder
2. Add your API key to the file:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
   ⚠️ **Important**: Replace `your_actual_api_key_here` with your real API key

### Step 5: Run the Chatbot

```bash
streamlit run app.py
```

The chatbot will open in your default web browser at `http://localhost:8501`

## 🎯 How to Use

1. **Start a Conversation**: Type your message in the chat input box at the bottom
2. **Send Your Message**: Press Enter or click the send button
3. **Wait for Response**: The AI will think and respond (you'll see a "Thinking..." spinner)
4. **Continue Chatting**: Keep the conversation going! The chatbot remembers your chat history
5. **Clear History**: Use the sidebar to clear your chat history if needed

## 📁 Project Structure

```
basic_Chatbot/
├── app.py              # Main chatbot application
├── requirements.txt    # Python dependencies
├── Readme.md          # This file
├── .env               # Your API key (create this file)
└── .venv/             # Virtual environment folder
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in your project root with:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### Available AI Models

The chatbot currently uses `gemini-2.5-flash`, but you can change it in `app.py`:

```python
# Change this line in app.py
model = genai.GenerativeModel('gemini-2.5-flash')

# Other available models:
# - 'gemini-pro' (older, but still good)
# - 'gemini-1.5-flash' (faster, less capable)
```

## 🛠️ Troubleshooting

### Common Issues

1. **"API Key not found" error**:
   - Make sure you created the `.env` file
   - Check that your API key is correct
   - Ensure the file is in the same folder as `app.py`

2. **"Module not found" errors**:
   - Make sure you activated your virtual environment
   - Run `pip install -r requirements.txt` again

3. **Chatbot not responding**:
   - Check your internet connection
   - Verify your API key is valid
   - Make sure you haven't exceeded your API quota

4. **Streamlit not opening**:
   - Try running `streamlit run app.py --server.port 8501`
   - Check if port 8501 is already in use

### Getting Help

- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Visit [Google AI Studio](https://makersuite.google.com/) for API help
- Ensure your Python version is 3.8 or higher

## 🎨 Customization

### Changing the UI

You can customize the appearance by modifying these parts in `app.py`:

- **Page title**: Change `page_title="AI Chatbot"`
- **Page icon**: Change `page_icon="🤖"`
- **Chat input placeholder**: Change `"Ask me anything..."`

### Adding Features

Some ideas for enhancement:
- Add conversation export functionality
- Implement different AI personalities
- Add file upload capabilities
- Create conversation themes

## 📚 Learning Resources

- **Streamlit**: [Official Documentation](https://docs.streamlit.io/)
- **Google Gemini**: [API Documentation](https://ai.google.dev/docs)
- **Python**: [Official Tutorial](https://docs.python.org/3/tutorial/)
- **Environment Variables**: [Python-dotenv Guide](https://pypi.org/project/python-dotenv/)

## 🤝 Contributing

Feel free to:
- Report bugs or issues
- Suggest new features
- Improve the documentation
- Share your customizations

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Google** for providing the Gemini AI API
- **Streamlit** for the amazing web framework
- **Open Source Community** for the supporting libraries

---

**Happy Chatting! 🤖✨**

If you found this project helpful, consider giving it a star ⭐!
