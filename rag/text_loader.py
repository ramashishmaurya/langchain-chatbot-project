from langchain_community.document_loaders import TextLoader 

loader = TextLoader('cricket.txt' ,encoding='utf-8')

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
model = ChatOllama(model='llama3')
parser = StrOutputParser()
docs = loader.load()


from langchain_core.runnables import RunnableLambda
def prom():
    return {'topic':docs[0].page_content}

runnable = RunnableLambda(prom)


prompts = PromptTemplate(
    template='give me summary of this text in 5 line \n  {topic}' , 
    input_variables=['topic']
)

chain = runnable | prompts | model | parser

print(chain.invoke({
}))