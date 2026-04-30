from langchain_community.document_loaders import PyPDFLoader

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
model = ChatOllama(model='llama3')
parser = StrOutputParser()

loader = PyPDFLoader('roadmap.pdf')
docs = loader.load()

lazy_load = loader.lazy_load() 

print(len(docs))

print(docs[1].model_extra)

