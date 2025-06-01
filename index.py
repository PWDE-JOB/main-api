from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_PRIVATE_KEY")


@app.get("/")
async def root ():
    return {"message":"working"}


from models.model import inputSignupEmployee
#Authentication Process
@app.post("/signupEmployee") # signup for employee
async def signUp(user: inputSignupEmployee):
    role = "employee"
    #signing up the user
    try:
        supabase: Client = create_client(url, key)
        response = supabase.auth.sign_up(
            {
                "email": user.email, 
                "password": user.password,
            }
        )
        # print(supabase.auth.get_session())
    except Exception as e:
        return{
            "Status":"ERROR",
            "Message":"Signing Up Failed",
            "Details": f"{e}"
        }
    
    if response:
        try:
            supabase_insert: Client = create_client(url, key) #re created a suapsbe client for insertion (Current band aid fix)
            user_data = { # Structure the data to be inserted
                "user_id": response.user.id,
                "first_name": user.first_name,
                "middle_name": user.middle_name,
                "last_name": user.last_name,
                "disability": user.disability,
                "role": role,
                "skills":str(user.skills)
            }
            
            # print(user_data)
            
            #Insert data "suer_data" to the table
            insert_data = supabase_insert.table("employee").insert(user_data).execute()
            
            return{
                "Status": "Successfull",
                "Message": f"{user.first_name}has been successfully signed up",
                "Details": f"{insert_data}"
            }
        except Exception as e:
            return{
                "Status":"ERROR",
                "Message:":"Internal error. Data insertion failed",
                "Details": f"{e}"
            }

from models.model import inputSignupEmployer
@app.post("/signupEmployer") # signup for employer
async def signUp(user: inputSignupEmployer):
    role = "employer"
    #signing up the user
    try:
        supabase: Client = create_client(url, key)
        response = supabase.auth.sign_up(
            {
                "email": user.email, 
                "password": user.password,
            }
        )
        # print(supabase.auth.get_session())
    except Exception as e:
        return{
            "Status":"ERROR",
            "Message":"Signing Up Failed",
            "Details": f"{e}"
        }
    
    if response:
        try:
            supabase_insert: Client = create_client(url, key) #re created a suapsbe client for insertion (Current band aid fix)
            user_data = { # Structure the data to be inserted
                "user_id": response.user.id,
                "first_name": user.first_name,
                "middle_name": user.middle_name,
                "last_name": user.last_name,
                "email":user.email,
                "role": role,
            }
            
            # print(user_data)
            
            #Insert data "suer_data" to the table
            insert_data = supabase_insert.table("employers").insert(user_data).execute()
            
            return{
                "Status": "Successfull",
                "Message": f"{user.first_name}has been successfully signed up",
                "Details": f"{insert_data}"
            }
        except Exception as e:
            return{
                "Status":"ERROR",
                "Message:":"Internal error. Data insertion failed",
                "Details": f"{e}"
            }

from models.model import loginCreds           
@app.post("/login")
async def login(user: loginCreds):
    supabase: Client = create_client(url, key)
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": user.email,
                "password": user.password
            }
        )
        return{
            "Status":"Successfull",
            "Message": "Login Successfull",
            "Details": f"{response}"
        }
    except Exception as e:
        return{
            "Status": "ERROR",
            "Message": "Internal Server Error"
        }