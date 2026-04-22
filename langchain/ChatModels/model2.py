from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
 
model = ChatAnthropic(model_name='abc.n.1' , max_tokens_to_sample=123 ) # it is create the token sample of 

chat = model.invoke('what is machine learning') # send the query and get the result 

print(chat.content)
