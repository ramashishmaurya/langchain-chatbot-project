from langchain_huggingface import HuggingFaceEmbeddings

embedding= HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')
# embedding is that convert the normal string into the vector based on the semantic values semantic values as well 
text = 'who is donald trump'
vector = embedding.embed_query(text)
print(str(vector)) 
# we are receiving the values here right getting the embedded values 
vector.query



