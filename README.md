# 🤖 Groq Chatbot (Python)

A modular chatbot built using **Groq API** and **Python**, designed with clean architecture, secure API handling, and industry-level project structure.

---

## 🚀 Features

* ⚡ Fast responses using Groq API
* 🧠 Uses `llama-3.1-8b-instant` model
* 🔐 Secure API key handling using `.env`
* 🧱 Modular structure (industry standard)
* 💻 CLI-based chatbot

---

## 📁 Project Structure

```
groq-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── chatbot.py
│   ├── config.py
│
├── env/                # Virtual environment (not pushed)
├── .env                # API key (not pushed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

* Python 3.8+
* Git installed
* Groq API key

---

## 🔐 Setup API Key (IMPORTANT)

1. Create a file named `.env` in the root folder
2. Add your API key:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Do NOT add spaces
❌ WRONG → `GROQ_API_KEY = key`
✅ CORRECT → `GROQ_API_KEY=key`

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
python -m venv env
```

---

### 3. Activate Virtual Environment ⚠️ (VERY IMPORTANT)

```
env\Scripts\activate
```

👉 You should see `(env)` in terminal

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
python3 -m venv env
```

---

### 3. Activate Virtual Environment ⚠️

```
source env/bin/activate
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
3. Model processes the request
4. Response is printed back

---

## 🧠 Code Explanation

* **main.py** → Runs the chatbot loop
* **chatbot.py** → Sends request to Groq API
* **config.py** → Loads API key from `.env`

---

## ⚠️ Common Errors & Fixes

### ❌ ModuleNotFoundError: No module named 'groq'

✔️ Fix:

```
env\Scripts\activate
pip install -r requirements.txt
```

---

### ❌ API Key Not Found

✔️ Fix:

* Create `.env` file
* Add:

```
GROQ_API_KEY=your_key
```

---

### ❌ ModuleNotFoundError: No module named 'app'

✔️ Fix:

```
python -m app.main
```

---

### ❌ requirements.txt not found

✔️ Fix:

* Make sure you are in root folder
* Run:

```
dir   (Windows)
ls    (Mac/Linux)
```

---

### ❌ Virtual Environment Not Activated

✔️ Fix:

```
env\Scripts\activate      (Windows)
source env/bin/activate   (Mac/Linux)
```

---

## 🧪 Example

```
🤖 Groq Chatbot (type 'exit' to quit)

You: Hello
Bot: Hi! How can I help you today?
```

---

## 🔒 Security

* `.env` is ignored using `.gitignore`
* Never share API keys
* Always use environment variables

---

## 🚀 Future Improvements

* 🧠 Add memory
* 🎭 Add personality
* 🌐 Build API (FastAPI)
* 🖥️ Add frontend

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
