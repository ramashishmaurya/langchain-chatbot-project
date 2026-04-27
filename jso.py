from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


model = ChatOllama(model='llama3')
parser = JsonOutputParser()
templates = PromptTemplate(
 template='give me city , name and functional person \n {formate_instruction}' , 
 input_variables=[] , 

 partial_variables={'formate_instruction':parser.get_format_instructions()
                    }
)

# this is going to work when the u want to deal with the json formate right 
prompts = templates.format() # this is why here because this is going to return the json formate 


chain = templates |model | parser  # this is chnain is making the things easier right 


# result = model.invoke(prompts)
# final_result = parser.parse(result.content)
# print(final_result)

result = chain.invoke({})
print(result)