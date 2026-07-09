import psycopg2
from dotenv import load_dotenv
import os
import time
load_dotenv()


# def get_db_connection():
#     conn = psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT"),
#         user=os.getenv("DB_USER"),
#         database=os.getenv("DB_NAME"),
#         password=os.getenv("DB_PASSWORD")
#     )

#     return conn



def get_db_connection():
    retries = 10
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                user=os.getenv("DB_USER"),
                database=os.getenv("DB_NAME"),
                password=os.getenv("DB_PASSWORD")
            )
            return conn

        except Exception as e:
            print("Database not ready, waiting...")
            retries -= 1
            time.sleep(3)
    raise Exception("Database connection failed")

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS form_submission(
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(100),
        middlename VARCHAR(100),
        lastname VARCHAR(100),
        fathername VARCHAR(100),
        mothername VARCHAR(100),
        age INT,
        emailid VARCHAR(100),
        mobilenumber VARCHAR(20),
        qualification VARCHAR(70),
        department VARCHAR(70),
        cgpa FLOAT,
        city VARCHAR(70),
        state VARCHAR(70),
        pincode INT,
        employeed BOOLEAN,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()