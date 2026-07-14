
# In this file we just do multiple data validation 
# if the age of the patient is more then 60 then in contact details they must have the emergency phone number


from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name : str
    age : int
    weight : float
    married : bool
    email : EmailStr
    allergies : List[str]
    contact : Dict[str, str]

    @model_validator(mode='after')
    def validate_emerfency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('not have the emergency contact')
        return model

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.contact)

    print('updated')

patient_info= {'name':'venom','age':79, 'weight':85.2, 'married': False, 'email': 'good@gmail.com',
                   'allergies':['pollen'], 'contact':{'phone':'5641457','emergency':'5554455'}}


patient2 = Patient(**patient_info)

update_patient_data(patient2)
    