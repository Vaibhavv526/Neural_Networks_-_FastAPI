from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator 
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name: str
    email: EmailStr
    age : int
    weight: float
    married : bool

    allergies : List[str]
    contact : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
          
          valid_domain = ['company.com','HDFC.com']

          doamin_name = value.split('@')[-1]

          if doamin_name not in valid_domain:
                raise ValueError('Not a valid employee')
          return value

  
def update_patient_data(Patient : patient):
        print(Patient.name)
        print(Patient.email)

        print('updated')

patient_info = {'name': 'Vaibhav', 'age': 20, 'email':'Vaibhav@company.com','linkedin_url': 'http://Linkedin.com',
                'weight':50.5,'married':True,'allergies': ['dust', 'pollen'], 'contact': {'phonr':'665652'}}

patient1 = patient(**patient_info)

update_patient_data(patient1)
