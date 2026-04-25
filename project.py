from langchain_ollama import ChatOllama

llm = ChatOllama(model='llama3')

import streamlit as st 

st.header('Reasearch Tools')
input_text = st.text_input('Enter the query_here')

if st.button('summarize'):
    chat = llm.invoke(input_text)
    st.write(chat.content)


