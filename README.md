# Resume-Rag-Chatbot
A Retrieval-Augmented Generation (RAG) chatbot that answers questions from a resume PDF using LangChain, ChromaDB, Hugging Face Embeddings, and Ollama (Llama 3.2).

# Resume RAG Chatbot using LangChain, ChromaDB & Ollama

## 📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on a resume PDF.

Instead of relying on the LLM's memory, the chatbot retrieves relevant information from the uploaded resume using vector embeddings and ChromaDB, then generates an accurate response using the Llama 3.2 model running locally with Ollama.

---

## 🚀 Features

* Load Resume PDF
* Text Chunking
* Hugging Face Embeddings
* Chroma Vector Database
* Semantic Search
* Local LLM (Llama 3.2 via Ollama)
* Interactive Question Answering
* Retrieval-Augmented Generation (RAG)

---

## 🛠 Technologies Used

* Python
* LangChain
* Ollama
* Llama 3.2
* ChromaDB
* HuggingFace Embeddings
* Sentence Transformers
* PyPDF
* Recursive Character Text Splitter

---

## 📂 Project Workflow

Resume PDF

↓

PyPDFLoader

↓

Text Splitter

↓

HuggingFace Embeddings

↓

ChromaDB

↓

Retriever

↓

Llama 3.2 (Ollama)

↓

Answer

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/Resume-RAG-Chatbot.git
```

Go to the project

```bash
cd Resume-RAG-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

Download from:

https://ollama.com

Download the model

```bash
ollama pull llama3.2
```

Run the chatbot

```bash
python app.py
```

---

## Example

Question

```
What are your technical skills?
```

Answer

```
Python, SQL, Scikit-learn, Machine Learning, Data Analysis...
```

---

## Future Improvements

* Streamlit Web UI
* Chat History
* Multiple PDF Support
* Resume Upload
* FAISS Support
* Hybrid Search
* Conversation Memory

---

## Author

Prajakta Bagade
