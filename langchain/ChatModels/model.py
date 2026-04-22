from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

models  = ChatOpenAI(model='chatgptmodel' , temperature=0.3, max_completion_tokens=120)

chat = print(f'this is a modelchar {models}')
print(chat.content)
