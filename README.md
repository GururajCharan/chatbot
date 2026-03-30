# 🤖 AI Chatbot using LangChain & Streamlit

An interactive AI chatbot application built using **LangChain**, **Google Gemini API**, and **Streamlit**. This project allows users to have real-time conversations with an AI model through a simple and intuitive web interface.

---

## 🚀 Features

* 💬 Real-time chatbot interaction
* 🧠 Powered by Google Gemini (via LangChain)
* ⚡ Fast and responsive UI using Streamlit
* 🔐 Environment variable support for secure API key handling
* 📦 Modular and easy-to-understand code structure

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Generative AI (Gemini)
* dotenv

---

## 📁 Project Structure

```
lproj/
│── main.py
│── requirements.txt
│── .env
│── .gitignore
│── files/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/GururajCharan/chatbot.git
cd chatbot
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API key

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```
streamlit run main.py
```
