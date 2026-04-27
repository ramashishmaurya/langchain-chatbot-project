from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser , StrOutputParser
from langchain_core.prompts import PromptTemplate
model = ChatOllama(model='llama3')
parser2 = StrOutputParser()
parser = JsonOutputParser()
templates = PromptTemplate(
    template='give me name city education \n {call_output}' , 
    input_variables=[] , 
    partial_variables={
        'call_output':parser.get_format_instructions()
    }
)

templates2 = PromptTemplate(
    template='what is full form of {topic}' , 
    input_variables=['topic']
)

chain2 = templates2 | model  | parser2

result2 = chain2.invoke({
    'topic':'atm'
})
 
chain = templates | model | parser 

result = chain.invoke({})

print(result2)

chain2.get_graph().print_ascii()



