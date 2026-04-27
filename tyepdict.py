from langchain_ollama import ChatOllama
from typing import TypedDict , Annotated 

model = ChatOllama(model='llama3')

# schema 
class revies(TypedDict):
    summary:Annotated[str ,'thi is the briief about the sentences '] 
    sentiment : str 

new_model = model.with_structured_output(revies)

result = new_model.invoke('i am good a boys i do stufdy well and always comes firts for my right also give sentiment like good bad ')

print(result['summary'])
print(result['sentiment'])
