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
from models.model import inputSignupEmployer
#Authentication Process

# Signup for employee and employer
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
from redis_server.redis_client import redis
import json

#On this login, auth_userID needs to be retrieve on the client side emaning frontend so it can be use on the other endpoints
        
@app.post("/login-employee")
async def login(user: loginCreds):
    supabase: Client = create_client(url, key)
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": user.email,
                "password": user.password
            }
        )

        # Get the session
        session_key = response.session

        if session_key:
            access_token = session_key.access_token
            refresh_token = session_key.refresh_token
            auth_userID = response.user.id

            session_data = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }

            # Check if the user is in the employee table
            employee_check = supabase.table("employee").select("*").eq("user_id", auth_userID).single().execute()

            if employee_check.data:  # check for presence of data
                # Store session in Redis with a key prefix
                await redis.set(auth_userID, json.dumps(session_data), ex=1000)

                return {
                    "Status": "Success",
                    "Message": "Login successful. Session stored in Redis.",
                    "App User ID": auth_userID,
                    "Debug Session Key": f"session:{auth_userID}",
                    "Stored User ID": auth_userID
                }
            else:
                return {
                    "Status": "ERROR",
                    "Message": "User is not an employee"
                }
        else:
            return {
                "Status": "ERROR",
                "Message": "No session returned"
            }

    except Exception as e:
        return {
            "Status": "ERROR",
            "Message": "Internal Server Error",
            "Details": str(e)
        }

         
@app.post("/login-employer")
async def login(user: loginCreds):
    supabase: Client = create_client(url, key)
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": user.email,
                "password": user.password
            }
        )

        # Get the session
        session_key = response.session

        if session_key:
            access_token = session_key.access_token
            refresh_token = session_key.refresh_token
            auth_userID = response.user.id

            session_data = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }

            # Check if the user is in the employee table
            employee_check = supabase.table("employers").select("*").eq("user_id", auth_userID).single().execute()

            if employee_check.data:  # check for presence of data
                # Store session in Redis with a key prefix
                await redis.set(auth_userID, json.dumps(session_data), ex=1000)

                return {
                    "Status": "Success",
                    "Message": "Login successful. Session stored in Redis.",
                    "App User ID": auth_userID,
                    "Debug Session Key": f"session:{auth_userID}",
                    "Stored User ID": auth_userID
                }
            else:
                return {
                    "Status": "ERROR",
                    "Message": "User is not an employee"
                }
        else:
            return {
                "Status": "ERROR",
                "Message": "No session returned"
            }

    except Exception as e:
        return {
            "Status": "ERROR",
            "Message": "Internal Server Error",
            "Details": str(e)
        }

        
#Password reset to be followded after this week

#profile management
@app.get("/view-profile/{auth_userID}")
async def viewProfile(auth_userID: str):
    try:
        supabase = create_client(url, key)
        
        # print(f"Fetching profile for user_id: {auth_userID}")
        
        #Checking both tables if the user is an employee or employer
        
        response_employer = supabase.table("employers").select("*").eq("user_id", auth_userID).single().execute()
        
        if response_employer.data:
            return {"Profile": response_employer.data}
        
        response_employee = supabase.table("employee").select("*").eq("user_id", auth_userID).single().execute()
        
        if response_employee.data:
            return {"Profile": response_employee.data}
        
        # Not found in either table
        return {
            "Status": "ERROR",
            "Message": "User profile not found in employers or employees tables"
        }
    except Exception as e:
        print(f"Error fetching profile: {e}")
        return {
            "Status": "ERROR",
            "Message": "Internal Server Error",
            "Details": str(e)
        }