from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
 
templates =''' '''
llm = ChatOllama(model='llama3')

import streamlit as st 

st.header('Reasearch Tools')
input_text = st.text_input('Enter the query_here')

# this is simple a chain models right 
if st.button('summarize'): 
    chain = templates | llm  # this is chain in langchain 
    chat = llm.invoke(input_text) # invoke here
    # gives the input in this parameters
    chat2 = chain.invoke({
        'p1':'person'  , 
        'p2':'person2'
    })
    st.write(chat.content)


