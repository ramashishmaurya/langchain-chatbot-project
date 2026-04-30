from langchain_community.document_loaders import WebBaseLoader

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
from langchain_ollama import ChatOllama
prompts = PromptTemplate(

    template='answer the following  \n {question}  from the following text \n {text}' , 
    input_variables=['question' ,'text']
)
model = ChatOllama(model='llama3')

url = 'https://www.amazon.in/OnePlus-15R-Snapdragon%C2%AE-Personalised-Game-changing/dp/B0FZT1D63F/ref=sr_1_1_sspa?crid=3A7TF9EPR7HXD&dib=eyJ2IjoiMSJ9.QxZzGJQIEa_EkL1tww2tVhRS1huV9u-uM7ClkgMjB8lFiw7FQrX-eR00eXgNd6S-E7MiBE4nNKq1ZS934Oq1Ti50ymLZ-UR9lOEiDIHXdbYiGm977QBNRDFYhCmP1h_dvAD0VzGKPqd730LzjZwHFw8YvUjJQNEWHKVl6JPTqjLuYA9_KCcUzMfXAayzleLGxuIroD69tdYtuYIXYAEpBfs_1uM0gDrPvGF-SIv9XZY.sDAd_Nbc1qImswN9WoFBer2jiY_MAhbGkI3Yj34PEiU&dib_tag=se&keywords=phones%2Bunder%2B30k&qid=1777470729&sprefix=phines%2B%2Caps%2C367&sr=8-1-spons&aref=LfQgya39V3&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

loader = WebBaseLoader(url)

docs = loader.load()



chain = prompts | model | parser 

print(chain.invoke({
    'question':'what is name of model' , 
    'text':docs[0].page_content
}))
 
