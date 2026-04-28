from langchain_ollama import ChatOllama
from typing import TypedDict , Annotated  , Optional

model = ChatOllama(model='llama3')

# schema 
class revies(TypedDict):
    pros:Annotated[Optional[list[str]] ,'write down the pros in this list']
    key_theme = Annotated[list[str] ,'write the keys theme of  in revies give me in list ']
    summary:Annotated[str ,'thi is the briief about the sentences '] 
    sentiment : Annotated[str , 'Return the sentiments reviews either positive , negative or neutral']

new_model = model.with_structured_output(revies)

result = new_model.invoke('i am good a boys i do stufdy well and always comes firts for my right also give sentiment like good bad ')
print(result)
