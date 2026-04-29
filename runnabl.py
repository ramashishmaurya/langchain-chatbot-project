from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence , RunnableParallel

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
    template='generates the twits about {topic}' , 
    input_variables=['topic']
)

prompts1 = PromptTemplate(
    template='generate the post for linkedin {topic}' , 
    input_variables=['topic']
)
# runnable parameter help us to combine to models 

parr_chain = RunnableParallel({
    'tweets':RunnableSequence(prompts ,model ,parser) , 
    'linkedin':RunnableSequence(prompts1,model ,parser)
}
)

result = parr_chain.invoke({
    'topic':'AI'
})

print(result['tweets'])
print('**************************')
print(result['linkedin'])

from langchain_core.runnables import RunnablePassthrough

passthrou = RunnablePassthrough() 

