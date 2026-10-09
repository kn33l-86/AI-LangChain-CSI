# Odyssey AI Chatbot 🤖

Odyssey is an AI chatbot built using Python, LangChain, Groq and Streamlit. The main idea behind this project was to understand how LLMs work with LangChain and how to turn a basic terminal chatbot into a proper web-based chatbot.

It uses Groq to run the language model, LangChain to handle prompts and conversation history, and Streamlit for the frontend.

## Features

* **AI Chatbot:** Answers questions and explains concepts in a simple way.
* **Conversation Memory:** Remembers previous messages during the conversation so the responses have context.
* **Streaming Responses:** Displays the response as it is generated instead of making the user wait for the entire answer.
* **Web Interface:** Uses Streamlit to provide a simple chat interface.
* **Secure API Key Handling:** Uses environment variables to store the Groq API key instead of hardcoding it into the code.

## Tech Stack

* Python
* Streamlit
* LangChain
* LangChain Groq
* Groq API
* python-dotenv

## Project Structure

```text
ai-langchain-csi/
│
├── app.py             # Streamlit frontend and chat memory
├── main.py            # LangChain setup and AI model
├── requirements.txt   # Required Python libraries
├── .env               # API key and environment variables
├── .venv/             # Python virtual environment
└── README.md
```

## How It Works

The project is divided into two main parts.

**1. main.py**

This file handles the AI side of the project. It loads the Groq API key, initializes the language model, creates the prompt template and combines everything into a LangChain chain.

It also supports conversation history and streaming responses.

**2. app.py**

This file handles the Streamlit interface. It displays previous messages, takes user input and sends the question along with the conversation history to the LangChain chain.

The generated response is displayed in the chat interface using Streamlit's `st.write_stream()`.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ai-langchain-csi
```

Replace `<your-repository-url>` with the URL of this repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If you're using Command Prompt instead of PowerShell:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the API key

Create a file named `.env` in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual API key from the Groq console.

Keep this file private and do not upload it to GitHub.

### 5. Run the application

Start the Streamlit app using:

```bash
streamlit run app.py
```

Streamlit will provide a local URL where the chatbot can be accessed through your browser.

## Environment Variables

| Variable       | Description                                    |
| -------------- | ---------------------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq language model |

## Model Configuration

The project currently uses `openai/gpt-oss-20b` through Groq.

The model configuration includes a temperature of `0.7` and a maximum output length of `1024` tokens.

These settings can be changed in `main.py` depending on the requirements.

## Requirements

The `requirements.txt` file contains the Python libraries required to run the project. Install them using:

```bash
pip install -r requirements.txt
```

The `.venv` folder contains the local Python environment and does not need to be uploaded to GitHub. It can be recreated using the setup steps above.

## What I Learned

While building this project, I got to work with LangChain's prompt templates, message history, output parsers and LCEL chains. I also learned how to stream LLM responses, connect a language model through an API and use Streamlit to build a basic interactive web application.

The project helped me understand how the different parts of an AI chatbot fit together, from handling user input to generating and displaying the final response.

## Future Improvements I'd like to do in future

* Add document-based question answering using RAG.
* Improve conversation memory and allow users to manage chat sessions.
* Add options to clear or start a new conversation.
* Improve the UI and add more customization options.
* Deploy the application so it can be accessed online.

---

Built as a learning project while exploring Python, LangChain and LLM application development.
