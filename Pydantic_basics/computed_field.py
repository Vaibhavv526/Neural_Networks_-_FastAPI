# when we habe to calculate some data from the provided data by the user we use computed field

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age : int
    weight : float
    height: float
    married : bool
    email: EmailStr
    allergies: List[str]
    contact : Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.contact)
    print('BMI',patient.calculate_bmi)

    print('updated')

patient_info= {'name':'venom','age':79, 'weight':85.2, 'height':5.8,'married': False, 'email': 'good@gmail.com',
                   'allergies':['pollen'], 'contact':{'phone':'5641457','emergency':'5554455'}}


patient2 = Patient(**patient_info)

update_patient_data(patient2)