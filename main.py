import os
import streamlit as st
# import pandas as pd
import pickle
import time
from langchain import OpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

st.title('News Research Tool 📉')
st.sidebar.title('News Article URLs 📰🗞')
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_click = st.sidebar.button('Process URLs')
file_path = 'faiss_store_openai.pkl'
main_placeholder = st.empty()
llm = OpenAI(temperature = 0.9, max_tokens = 500)

if process_url_click:
    # load Data
    loader = UnstructuredURLLoader(urls = urls)
    data = loader.load()
    main_placeholder.text('Data Loading...Started...✅✅✅✅')

    # Split Data
    text_splitter = RecursiveCharacterTextSplitter(separators = ['\n\n','\n',',','.'],
                                   chunk_size = 1000)
    docs = text_splitter.split_documents(data)
    main_placeholder.text('Text Splitter Started...✅✅✅✅')

    # Create Embeddings and Save it to FAISS
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text('Embedding Vector start Building...✅✅✅✅')

    # Save FAISS index to the file
    with open(file_path, 'wb') as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.input_text('Question: ')
if query:
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain(llm = llm, retriever = vectorstore.as_retriever())
            chain({'question':query}, return_only_outputs = True)
            # {"answer":"", "sources":[]}
            st.header('Answer')
            st.write(chain['answer'])

            # Display Sources if available
            sources = chain.get('sources','')
            if sources:
                st.subheader("Sources: ")
                sources_list = sources.split('\n')
                for source in sources_list:
                    st.write(source)
