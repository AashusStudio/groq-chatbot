# 🤖 Groq Chatbot (Python)

A modular and production-style chatbot built using **Groq API** and **Python**, designed with clean architecture, secure API handling, and industry-level project structure.

---

## 🚀 Features

* ⚡ Fast AI responses using Groq API
* 🧠 Uses `llama-3.1-8b-instant` model
* 🔐 Secure API key management using `.env`
* 🧱 Modular project structure (industry standard)
* 💻 CLI-based chatbot interface
* 📦 Easy to set up and run

---

## 📁 Project Structure

```
groq-chatbot/
│
├── app/
│   ├── __init__.py       # Marks app as a Python package
│   ├── main.py           # Entry point of the chatbot
│   ├── chatbot.py        # Core chatbot logic
│   ├── config.py         # Loads environment variables
│
├── .env                  # API key (not pushed to GitHub)
├── .gitignore            # Files to ignore
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## ⚙️ Prerequisites

Make sure you have:

* Python 3.8 or higher installed
* Git installed
* Groq API key (Get from Groq Console)

---

## 🔐 Setting Up API Key

1. Create a file named `.env` in the root directory
2. Add your API key like this:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Never share your API key publicly.

---

## 🪟 Windows Setup Guide

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/groq-chatbot.git
cd groq-chatbot
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

---

### 3. Activate Virtual Environment

```
venv\Scripts\activate
```

---

### 4. Install Dependencies

```
pip install -r requirements.txt
```

---

### 5. Run the Chatbot

```
python -m app.main
```

---

## 🍎 Mac/Linux Setup Guide

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/groq-chatbot.git
cd groq-chatbot
```

---

### 2. Create Virtual Environment

```
python3 -m venv venv
```

---

### 3. Activate Virtual Environment

```
source venv/bin/activate
```

---

### 4. Install Dependencies

```
pip install -r requirements.txt
```

---

### 5. Run the Chatbot

```
python3 -m app.main
```

---

## 💡 How It Works

1. User enters input in terminal
2. Input is sent to Groq API
3. The model (`llama-3.1-8b-instant`) processes the request
4. Response is returned and printed in terminal

---

## 🧠 Core Components Explained

* **main.py** → Handles user interaction loop
* **chatbot.py** → Sends request to Groq API and returns response
* **config.py** → Loads API key securely using environment variables

---

## ⚠️ Common Errors & Fixes

### ❌ ModuleNotFoundError: No module named 'app'

✔️ Fix:

```
python -m app.main
```

---

### ❌ API Key Not Found

✔️ Fix:

* Ensure `.env` file exists
* Check key name: `GROQ_API_KEY`

---

### ❌ Virtual Environment Not Activated

✔️ Fix:

```
venv\Scripts\activate   (Windows)
source venv/bin/activate (Mac/Linux)
```

---

### ❌ Dependencies Not Installed

✔️ Fix:

```
pip install -r requirements.txt
```

---

## 🧪 Example Usage

```
🤖 Groq Chatbot (type 'exit' to quit)

You: Hello
Bot: Hi! How can I help you today?

You: What is AI?
Bot: Artificial Intelligence (AI) refers to...
```

---

## 🔒 Security Note

* `.env` is ignored using `.gitignore`
* Never push API keys to GitHub
* Always use environment variables for secrets

---

## 🚀 Future Improvements

* 🧠 Add conversation memory
* 🎭 Add chatbot personality
* 🌐 Build FastAPI backend
* 🖥️ Add frontend UI

---

## 🤝 Contributing

Feel free to fork this repository and improve it.

---

## 📜 License

This project is open-source and free to use.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
