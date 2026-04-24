from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-Embedding-3-large' ,dimensions=32) # dimension means is that capture the more feature right 

chat = embedding.embed_query('What is capital of India')

print(str(chat))

documents =[
    'which is best food in india' , 
    'why india is not like usa'
]

chat2 = embedding.embed_documents(documents) # pass the multiple query simulataniosly

print(str(chat2))