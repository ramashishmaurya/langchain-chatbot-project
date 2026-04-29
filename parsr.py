from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model='llama3')

# 1st prompts 
templates = PromptTemplate(
    template='write the detail on this topic {topic} ' , 
    input_variables=['topic']
)
# #2nd prompts 
templates2 = PromptTemplate(
    template='write the 5 line summary on following text \n {text}' , 
    input_variables=['text']
)

# promts1 =templates.invoke({
#     'topic':'ai'
# })

# result = model.invoke(promts1)

# promts2 = templates2.invoke({
#     'text': result.content
# })

# chat = model.invoke(promts2)
# print(chat.content)

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
# this chain make all things automated right no need to invoke every template to promts 
chain = templates | model | parser | templates2 |model

result = chain.invoke({
    'topic':'ai'
})

print(result)


# Image save 
chain.get_graph().draw_png("chain_diagram.png")


print('tje vakues has to make sure ')




