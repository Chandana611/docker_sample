# Once the application process stops (server restart, crash, redeploy), the variable is cleared and all data is lost.

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class SubmitRequest(BaseModel):
    firstname: str
    middlename: Optional[str] = None
    lastname: str
    phone_number: int
    graduation: str
    cgpa: int
    city: str
    state: str
    address: Optional[str] = None
    email_id: Optional[str] = None
    employeed: bool

form_data = []

@app.post("/submit")
async def submit_form_data(request:SubmitRequest):
    form_data.append(request.dict())
    print(form_data)
    return {"message": "Form data submitted successfully!!!"}

@app.get("/get-data")
async def get_form_data():
    return form_data