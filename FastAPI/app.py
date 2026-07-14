# From now we  are start learning FastAPI

from fastapi import FastAPI, Path, HTTPException, Query

import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data 

@app.get("/")
def home():
    return {"message": "Patient Management System API !"}


@app.get("/about")
def about():
    return{"message": "API to manage your patient records"}


@app.get("/view")
def view():
    data = load_data()

    return data

@app.get('/patients/{patient_ID}')
def view_patient(patient_ID: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load the data
    data = load_data() 

    #logic
    if patient_ID in data:
        return data[patient_ID]
    raise HTTPException(status_code= 404, detail= 'Patient not found')

@app.get('/sort')
def sort_patients(sort_by : str= Query(..., description= 'Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order') ):

    valid_field = ['height', 'weight', 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail = f'Invalid field select from {valid_field} ')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
     
    sort_order = True if order== 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data