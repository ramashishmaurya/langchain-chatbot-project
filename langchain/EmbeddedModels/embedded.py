from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-Embedding-3-large' ,dimensions=32) # dimension means is that capture the more feature right 

# chat = embedding.embed_query('What is capital of India')

# print(str(chat))

documents =[
    'which is best food in india' , 
    'why india is not like usa'
]


query = 'which is not like usa' 

emb = embedding.embed_documents(documents) # pass the multiple query simulataniosly

chat2_query = embedding.embed_query(query)


scores =cosine_similarity([chat2_query],emb)[0] # cosine similiarity of that string right 

print(list(enumerate(scores)))

 
