from fastapi import FastAPI, Path, HTTPException,Query
from pydantic import BaseModel,Field, computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse

import json
app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(..., description='Id of the patiend', examples=['P001'])]
    name : Annotated[str,Field(..., description='Name of the patient',examples=['goku'])]
    city : Annotated[str, Field(..., description='City where your living')]
    age : Annotated[int, Field(..., gt =0, lt=100,description='your age')]
    gender :  Annotated[Literal['male','female'], Field(..., description='Gender of the patient')]
    height : Annotated[float,Field(..., gt=2.5, description='your height in mtrs')]
    weight : Annotated[float, Field(...,gt=13,description='your weight in kgs')]

    @computed_field
    @property

    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:

        if self.bmi <18.5:
            return 'underWeight'
        elif self.bmi <30:
            return 'Normal'
        else :
            return 'overWeight'

def load_data():
    with open('patients.json','r')as f:
        data = json.load(f)

        return data
    
def save_data(data):
    with open('patients.json','w')as f:
        json.dump(data,f)           # f means file
    
@app.get("/")
def hello():
    return {'message': 'Patient Managment system API'}


@app.post('/create')
def create_patient(patient : Patient):

    # load existing data 
    data = load_data()

    # check is the patient already exists

    if patient.id in data:
        raise HTTPException(status_code=400, detail = 'patient already exists')
    

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file

    save_data (data)

    return JSONResponse(status_code=201, content = {'message':'patient created successfully'})