from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

from langchain_ollama import ChatOllama

model = ChatOllama(model='llama3')

messages = [
    SystemMessage(content='you are helpful assistance ') , 
    HumanMessage(content='what is langchain') 

    ]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content)) # got the answer of ai right and stored into the model

print(messages )