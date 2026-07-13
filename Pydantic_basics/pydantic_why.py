from pydantic import BaseModel, EmailStr,Field, AnyUrl 
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):

    name :Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less then 50 character', examples=['vaibhav','Shipra'])]
    age : int = Field(gt=0, lt=100)
    email : EmailStr
    linkedin_url :AnyUrl
    weight: float = Field(gt =0)
    married: Annotated[Optional[bool],Field(default=None, description='Is the Patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length = 5)]
    contect: Dict[str, str]

def update_patient_data(Patient : patient):

    print(Patient.name)
    print(Patient.age)
    print(Patient.contect)
    print(Patient.linkedin_url)

    print('Updated')

patient_info = {'name': 'Vaibhav', 'age': 20, 'email':'Vaibhav@gmail.com','linkedin_url': 'http://Linkedin.com',
                'weight':50.5,'married':True, 'contect': {'phonr':'665652'}}

patient1 = patient(**patient_info)

update_patient_data(patient1)