# main.py 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from app.db import get_db_connection, create_table
from psycopg2.extras import RealDictCursor

# CI/CD deployment test - updated from local machine
app = FastAPI()

class SubmitRequest(BaseModel):
    firstname: str
    middlename: Optional[str] = None
    lastname: str
    fathername: str
    mothername: Optional[str] = None
    age: Optional[int] = None
    emailid: Optional[EmailStr] = None
    mobilenumber: str
    qualification: str
    department: Optional[str] = None
    cgpa: float
    city: str
    state: str
    pincode: Optional[int] = None
    employeed: bool

@app.on_event("startup")
def startup():

    create_table()

    print("Table checked/created successfully")

@app.post("/submit-datadb")
async def submit_data_indb(request: SubmitRequest):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO form_submission(
                firstname, middlename, lastname, fathername, mothername, age, emailid, mobilenumber, qualification, department, cgpa, city, state, pincode, employeed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            request.firstname,
            request.middlename,
            request.lastname,
            request.fathername,
            request.mothername,
            request.age,
            request.emailid,
            request.mobilenumber,
            request.qualification,
            request.department,
            request.cgpa,
            request.city,
            request.state,
            request.pincode,
            request.employeed
        ))
        conn.commit()
        return {
            "message":"Form submitted successfully"
        }   
    except Exception as e:
        if conn:
            conn.rollback()    
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()




@app.get("/get-form-data")
async def getform_dbdata():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM form_submission")
        rows = cursor.fetchall()
    
        cursor.close()
        conn.close()

        return rows
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
