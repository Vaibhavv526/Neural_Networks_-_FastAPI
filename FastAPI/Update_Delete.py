from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse
import json


app = FastAPI()


# -------------------- Patient Model --------------------

class Patient(BaseModel):
    id: Annotated[
        str,
        Field(
            ...,
            description="Id of the patient",
            examples=["P001"]
        )
    ]

    name: Annotated[
        str,
        Field(
            ...,
            description="Name of the patient",
            examples=["Goku"]
        )
    ]

    city: Annotated[
        str,
        Field(
            ...,
            description="City where you are living"
        )
    ]

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=100,
            description="Age of the patient"
        )
    ]

    gender: Annotated[
        Literal["male", "female"],
        Field(
            ...,
            description="Gender of the patient"
        )
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0.5,
            lt=3.0,
            description="Height in meters"
        )
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=13,
            description="Weight in kilograms"
        )
    ]


# -------------------- Patient Update Model --------------------

class PatientUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(default=None)
    ]

    city: Annotated[
        Optional[str],
        Field(default=None)
    ]

    age: Annotated[
        Optional[int],
        Field(default=None, gt=0, lt=100)
    ]

    gender: Annotated[
        Optional[Literal["male", "female"]],
        Field(default=None)
    ]

    height: Annotated[
        Optional[float],
        Field(default=None, gt=0.5, lt=3.0)
    ]

    weight: Annotated[
        Optional[float],
        Field(default=None, gt=13)
    ]


# -------------------- Load Data --------------------

def data_load():

    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


# -------------------- Save Data --------------------

def save_data(data):

    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


# -------------------- Home Endpoint --------------------

@app.get("/home")
def hello():

    return {
        "message": "Patient Management System"
    }


# -------------------- Update Patient Endpoint --------------------

@app.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):

    # Load existing data
    data = data_load()

    # Check if patient exists
    if patient_id not in data:

        raise HTTPException(
            status_code=404,
            detail="Patient is not present in the database"
        )

    # Get existing patient information
    existing_patient_info = data[patient_id]

    # Get only the fields sent by the user
    updated_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    # Update only the provided fields
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # Add ID temporarily for Pydantic validation
    existing_patient_info["id"] = patient_id

    # Validate updated patient data
    patient_pydantic_obj = Patient(
        **existing_patient_info
    )

    # Convert Pydantic object back to dictionary
    # Remove ID because patient_id is already the JSON key
    existing_patient_info = patient_pydantic_obj.model_dump(
        exclude={"id"}
    )

    # Update patient data
    data[patient_id] = existing_patient_info

    # Save updated data to patients.json
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient is updated successfully"
        }
    )
    
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load the data\
    data = data_load()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail = 'patient not found')
    
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=200, content='patient was deketed successfully')