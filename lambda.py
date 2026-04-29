from langchain_core.runnables import RunnableLambda , RunnableParallel , RunnableSequence , RunnablePassthrough

def word_counter(text):
    return len(text.split())

def addnumber(a  ):
    return a 

convert_into_runnable = RunnableLambda(word_counter)
convert_add_runnable = RunnableLambda(addnumber)

print(convert_into_runnable.invoke('Hi this is ashish here'))

print(convert_add_runnable.invoke(12))

# this is going to run the paraller 
runnableparallel = RunnableParallel(
    'run1' , RunnableSequence() , 
    'run2' , RunnableLambda(word_counter) , 
    'run3' , RunnablePassthrough() # when u dont want to send to the llm 
)
