from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence

# runnableSequence can run this sequence the 

from langchain_core.prompts import PromptTemplate


prompts2= PromptTemplate (
    template='this is topic  {topic}' ,
    input_variables=['topic']
)

prompts3 = PromptTemplate(
    template='what is full form {text}' , 
    input_variables=['text']
)

parser = StrOutputParser() 

model = ChatOllama(model='llama3') 
# this  model is running sequencial the values
#chain = RunnableSequence(prompts1 , model , parser , prompts2 ,model , parser)

chain =prompts2 |model | parser | prompts3 | model | parser

# result = chain.invoke({
#     'topic':'AI'
# })

prompts = PromptTemplate(
    template='generates the '
)


