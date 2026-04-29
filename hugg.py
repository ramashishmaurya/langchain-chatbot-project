from langchain_ollama import ChatOllama

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
from langchain.messages import Huma

prompts = PromptTemplate(
    template='write the full of {topic} in 2 line ' , 
    input_variables=['topic']
)

model = ChatOllama(model='llama3')

chain = prompts | model  |parser

result = chain.invoke({
    'topic':'ai'
})
print(result)