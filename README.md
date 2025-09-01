# News Research Tool Project

A lightweight and intuitive news research application built with **Streamlit** and **LangChain**.  
This tool fetches news articles from URLs, processes them via text splitting and embeddings, and stores the results in a **FAISS** vector database.  
Users can then query the content and receive precise, source-backed answers using a **RetrievalQAWithSourcesChain**.

---

## 🚀 Features
- Accepts news article URLs for input.  
- Loads and extracts content using `UnstructuredURLLoader`.  
- Splits long text via `RecursiveCharacterTextSplitter`.  
- Generates embeddings using `OpenAIEmbeddings`.  
- Stores and indexes embeddings efficiently with **FAISS**.  
- Supports user queries through a **RetrievalQAWithSourcesChain**, returning answers with source links.  

---

## ⚙️ Installation
- Clone the repository:  
  ```bash
  git clone https://github.com/1rishu0/News-Research-Tool-Project.git
  cd News-Research-Tool-Project

---

## 📂 Project Structure

- **`main.py`** – Main Streamlit application entry point  
- **`requirements.txt`** – Python dependencies required for the project  
- **`faiss_store_openai.pkl`** – Serialized FAISS index for storing embeddings  
- **`.env`** – Environment variables (not committed; contains your API key)  
- **`LICENSE`** – Project's open-source license (GPL-3.0) 

## 📸 Demo / Screenshots

![Image](https://github.com/user-attachments/assets/f5140384-6bce-4f38-a710-b6142e1d84cb)

---

## 📜 License

- This project is released under the GPL-3.0 license.
- See LICENSE for details.

---

## 💡 About

- Compact yet powerful implementation of semantic search over news content
- Combines modern LLM techniques with vector databases
- Builds research tools with accurate answer retrieval using LangChain, FAISS, and OpenAI

---

## 🙏 Acknowledgments

- Thanks to Codebasics for the helpful tutorial that guided this project.

- Quote from my project:

“I built a News Research Tool with Streamlit and LangChain that fetches news articles from URLs, processes them with text splitting and embeddings, and stores them in a FAISS vector DB. Users can query articles via a RetrievalQA chain to get precise, source-backed insights—showcasing my skills in LLMs and vector search.”
