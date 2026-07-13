# when we have to use one field inside the another field we use nested model 
from pydantic import BaseModel
from typing import List, Dict

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

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)