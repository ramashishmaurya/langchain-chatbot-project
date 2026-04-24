from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()
# temperature means how randomness you need in answer right if u need constand answer every for same input use it as temperature = 0 
models  = ChatOpenAI(model='chatgptmodel' , temperature=0.3, max_completion_tokens=120)

chat = print(f'this is a modelchar {models}')
print(chat.content)
