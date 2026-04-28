
import random
class sample:
    def __init__(self): # this is constructor 
        print('LLM is created')
    def predict(self , prompt):
        response = [
            'india is capital of delhi' , 
            'india is one of the best country ' , 
            'ai is growing rapidly'
        ]
        return {'response':random.choice(response)} # here is return fg

class PromptTemplates:
    def __init__(self , template , input_varibale):
        self.template = template
        self.input_variable = input_varibale
    
    def formate(self , user_dict):
        return self.template.format(**user_dict)


obj = PromptTemplates(
    template='this is a {topic}'  , 
    input_varibale=['topic']

)

result = obj.formate({
    'topic':'india'
})

llm = sample()
b = llm.predict(result)
print(b['response'])


