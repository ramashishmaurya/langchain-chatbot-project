from pydantic import BaseModel , Field

from typing import Optional  

class person(BaseModel):
    # contraint apply on this parameters 
    name:str 
    age:Optional[int] =None # this is optional right either use or not c
    cgpa :float =Field(gt=0 ,lt=10 , description='cgpa values range 0 to 10')
    

name = {'name':'ashish' ,'age':12 , 'cgpa':9}

b = person(**name)
make_dict = dict(b)
print(make_dict)
print(make_dict['name'])


