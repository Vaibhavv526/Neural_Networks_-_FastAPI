# how to export the pydantic model in python dictionary or Json dictionary

from pydantic import BaseModel

class Address (BaseModel):

    city : str
    state : str
    pin : int

address_dict = { 'city':'raipur', 'state':'CG','pin': 545562}
address1 = Address(**address_dict) 

class patient(BaseModel):

    name : str
    gender : str
    age : int
    address: Address

patient_dict = {'name': 'venom', 'gender':'male','age':41, 'address':address1}

patient1= patient(**patient_dict)

temp = patient1.model_dump(exclude=['name'])
temp_json = patient1.model_dump_json(include=['address'], exclude={'address':['state']})
print(temp_json)
print(temp)