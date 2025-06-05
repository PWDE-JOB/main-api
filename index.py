from fastapi import FastAPI, Request, HTTPException
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
service_key = os.getenv("SUPBASE_SERVICE_KEY")


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
                "auth_userID": auth_userID,
                "refresh_token": refresh_token
            }

            # Check if the user is in the employee table
            employee_check = supabase.table("employee").select("*").eq("user_id", auth_userID).single().execute()

            if employee_check.data:  # check for presence of data
                # Store session in Redis with a key prefix
                await redis.set(access_token, json.dumps(session_data), ex=None)

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
                "auth_userID": auth_userID,
                "refresh_token": refresh_token
            }

            # Check if the user is in the employee table
            employee_check = supabase.table("employers").select("*").eq("user_id", auth_userID).single().execute()

            if employee_check.data:  # check for presence of data
                # Store session in Redis with a key prefix
                await redis.set(access_token, json.dumps(session_data), ex=3600)

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

# functions for retriving session or to be speficifc the user ID
async def getAuthUserIdByToken(redis, access_token):
    value = await redis.get(access_token)
    if value:
        session_data = json.loads(value)
        return session_data.get("auth_userID")
    return None

async def getAuthUserIdFromRequest(redis, request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    
    access_token = token.split("Bearer ")[1]
    
    auth_userID = await getAuthUserIdByToken(redis, access_token)
    if not auth_userID:
        raise HTTPException(status_code=401, detail="Session not found in Redis")
    
    return auth_userID




# To send an authenticated request to the backend (e.g., /view-profile):
# Retrieve the access token (from localStorage, sessionStorage, or cookies).
# Add it to the request header as: Authorization: Bearer <access_token>.

# Example (using Fetch API):
#   
#    const accessToken = localStorage.getItem('access_token'); // or from a cookie
#   
#    fetch('http://localhost:8000/view-profile', {
#      method: 'GET',
#      headers: {
#        'Authorization': `Bearer ${accessToken}`
# }
# })

#profile management
@app.get("/view-profile")
async def viewProfile(request: Request):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
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

# Profile Update
#this will update only name, skills, and disability 
from models.model import updateEmployer, updateEmployee
@app.post("/update-profile/employer")
async def updateProfile(request: Request, update_employer: updateEmployer):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        supabase = create_client(url, service_key)
        
        # Check if the user is an employer
        search_employer = supabase.table("employers").select("user_id").eq("user_id", auth_userID).single().execute()
        
        if search_employer.data and search_employer.data["user_id"] == auth_userID:
            updated_details ={
                "first_name": update_employer.first_name,
                "middle_name": update_employer.middle_name,
                "last_name": update_employer.last_name
            }
            
            update_employer_res = supabase.table("employers").update(updated_details).eq("user_id", auth_userID).execute()
            
            if update_employer_res.data:
                return{
                     "Status": "Successfull",
                     "Message": "Update successfull"
                 }
            else:
                return {
                     "Status": "Error",
                     "Message": "Updating not Succesfull",
                     "Details": f"{update_employer_res}" 
                 }
        else:
            return{
                "Status": "Error",
                "Message": "Cant find user",
                "Details": f"{search_employer}" 
            }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Server Error",
            "Details": f"{e}"
        }



@app.post("/update-profile/employee")
async def updateProfile(request: Request, update_employee: updateEmployee):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        supabase = create_client(url, service_key)
        
        # Check if the user is an employer
        search_employee = supabase.table("employee").select("user_id").eq("user_id", auth_userID).single().execute()
        
        if search_employee.data and search_employee.data["user_id"] == auth_userID:
            updated_details ={
                "first_name": update_employee.first_name,
                "middle_name": update_employee.middle_name,
                "last_name": update_employee.last_name,
                "disability": update_employee.disability,
                "skills": str(update_employee.skills)
                
            }
            
            update_employee_res = supabase.table("employee").update(updated_details).eq("user_id", auth_userID).execute()
            
            if update_employee_res.data:
                return{
                     "Status": "Successfull",
                     "Message": "Update successfull"
                 }
            else:
                return {
                     "Status": "Error",
                     "Message": "Updating not Succesfull",
                     "Details": f"{update_employee_res}" 
                 }
        else:
            return{
                "Status": "Error",
                "Message": "Cant find user",
                "Details": f"{search_employee}" 
            }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Server Error",
            "Details": f"{e}"
        }

#job shii

#create jobs
# This endpoint is for empployers to be able create jobs, view al jobs listings they created, view a specific job listinsg details, delete, and update
from models.model import jobCreation
@app.post("/create-jobs")
async def createJob(job: jobCreation, request: Request):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        #check first if the user exist as an employer
        supabase: Client = create_client(url, service_key)
        search_id = supabase.table("employers").select("user_id").eq("user_id", auth_userID).single().execute()
        
        if search_id:
            # structure teh data to be created
            jobs_data = {
                "user_id": auth_userID,
                "title": job.title,
                "job_description": job.description,
                "skill_1": job.skill_1,
                "skill_2": job.skill_2,
                "skill_3": job.skill_3,
                "skill_4": job.skill_4,
                "skill_5": job.skill_5,
                "pwd_friendly": job.pwd_friendly,
                "salary": job.salary
            }
            
            insert_response = supabase.table("jobs").insert(jobs_data).execute()
            
            return{
                "Status": "Sucessfull",
                "Message": "Job has been created",
                "Details": f"{insert_response}"
            }
        else:
            return {
                "Status": "Error",
                "Message": "Maybe the employer dosen't exist"
            }
    except Exception as e:
        return{
            "Status": "Internal Server Error",
            "Message": "Some sort of error",
            "Details": f"{e}"
        }

@app.get("/view-all-jobs")
async def viewAllJobs(request: Request):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        supabase = create_client(url, key)
        
        all_jobs = supabase.table("jobs").select("*").eq("user_id", auth_userID).execute()
        
        if all_jobs:
            return {"jobs": all_jobs.data}
        
        return {
            "Status": "ERROR",
            "Message": "No Jobs Found"
        }
    except Exception as e:
        return{
            "Status": "ERROR",
            "Message": "Internal Server Error",
            "Details": f"{e}"
        }

@app.get("/view-job/{id}")
async def viewSpecificJob(request: Request, id: str):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        
        supabase = create_client(url, key)
        
        job = supabase.table("jobs").select("*").eq("user_id", auth_userID).eq("id", id).execute()
        
        if job:
            return {
                "Status": "Successfull",
                "Message": f"Job Number {id} Found",
                "Details": job.data
            }
        return {
            "Status": "Error",
            "Message": "Job Not Found"
        }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Error",
            "Details": f"{e}"
        }

@app.post("/delete-job/{id}")
async def deleteJob(request: Request, id: str):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        supabase = create_client(url, service_key)

        # Check if the user is an employer
        search_id = supabase.table("employers").select("user_id").eq("user_id", auth_userID).single().execute()

        if search_id.data and search_id.data["user_id"] == auth_userID:
            #delete the job
            delete_job = supabase.table("jobs").delete().eq("id", id).execute()
            # print(delete_job)
            
            if delete_job.data:  # check if any row was actually deleted
                return {
                    "Status": "Success",
                    "Message": f"Job {id} deleted successfully"
                }
            else:
                return {
                    "Status": "Error",
                    "Message": f"No job found with id {id} to delete.",
                    "Details": f"{delete_job}"
                }
        else:
            return {
                "Status": "Error",
                "Message": "Employer not found or not authorized."
            }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Server Error",
            "Details": f"{e}"
        }

from models.model import updateJob
@app.post("/update-job/{id}")
async def updateSpecificJob(request: Request, id: str, job: updateJob):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        supabase = create_client(url, service_key)

        # Check if the user is an employer
        search_id = supabase.table("employers").select("user_id").eq("user_id", auth_userID).single().execute()

        if search_id.data and search_id.data["user_id"] == auth_userID:
             #build the structure of the update json 
             new_data = {
                "user_id": auth_userID,
                "title": job.title,
                "job_description": job.description,
                "skill_1": job.skill_1,
                "skill_2": job.skill_2,
                "skill_3": job.skill_3,
                "skill_4": job.skill_4,
                "skill_5": job.skill_5,
                "pwd_friendly": job.pwd_friendly,
                "salary": job.salary
             }
             update_response = supabase.table("jobs").update(new_data).eq("id", id).execute()
            
             if update_response.data:
                 return{
                     "Status": "Successfull",
                     "Message": "Update successfull"
                 }
             else:
                 return {
                     "Status": "Error",
                     "Message": "Updating not Succesfull",
                     "Details": f"{update_response}" 
                 }
        else:
            return{
                "Status": "Error",
                "Message": "Cant find user",
                "Details": f"{search_id}" 
            }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Server Error",
            "Details":f"{e}"
        }
          
#MAIN ALGO WORKS (Content absed filtering + collaborative filtering)
import ast
@app.get("/reco-jobs")
async def reccomendJobs(request: Request):
    try:
        # Get the user details
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        supabase = create_client(url, key)

        # Fetch the user details
        search_user = supabase.table("employee").select("*").eq("user_id", auth_userID).single().execute()

        if not search_user or not search_user.data:
            return {
                "Status": "Error",
                "Message": "Can't find user"
            }

        # user_id = search_user.data.get("user_id")
        disability = search_user.data.get("disability")

        # Parse the skills
        user_skills_set = set()
        skills_raw = search_user.data.get("skills", "[]")
        try:
            skills_list = ast.literal_eval(skills_raw)
        except Exception:
            skills_list = []

        for skill in skills_list:
            if isinstance(skill, str):
                user_skills_set.add(skill.strip().lower())

        # Fetch jobs based on disability
        if disability == "None":
            jobs_response = supabase.table("jobs").select("*").execute()
            jobs_data = jobs_response.data or []
        else:
            jobs_response = supabase.table("jobs").select("*").eq("pwd_friendly", True).execute()
            jobs_data = jobs_response.data or []

        # Recommendations
        recommendations = []

        for job in jobs_data:
            # Extract job skills
            job_skills = []
            for i in range(1, 6):
                skill = job.get(f"skill_{i}", "")
                if isinstance(skill, str) and skill.strip():
                    job_skills.append(skill.strip().lower())

            job_skills_set = set(job_skills)

            # Calculate skill match score
            matched_skills_set = user_skills_set & job_skills_set
            matched_skills_count = len(matched_skills_set)

            if job_skills_set:
                skill_match_score = matched_skills_count / len(job_skills_set)
            else:
                skill_match_score = 0

            # Create a copy of the job details and add match data
            # Exclude jobs with zero match score
            if skill_match_score > 0:
                job_copy = job.copy()
                job_copy["skill_match_score"] = skill_match_score
                job_copy["matched_skills"] = list(matched_skills_set)
                recommendations.append(job_copy)
                
        # Sort and return top 5 recommendations
        recommendations.sort(key=lambda x: x["skill_match_score"], reverse=True)
        
        for job in recommendations:
            job_id = job["id"]

            # Check if this record already exists
            existing_record = supabase.table("employee_history").select("id").eq("user_id", auth_userID).eq("job_id", job_id).execute()

            if not existing_record.data:
                # Insert the new history record
                supabase.table("employee_history").insert({
                    "user_id": auth_userID,
                    "job_id": job_id
                }).execute()

        return {
            "recommendations": recommendations
        }

    except Exception as e:
        return {
            "error": str(e)
        }

# apply to a job
@app.post("/apply-job/{job_id}")
async def applyingForJob(job_id: str, request: Request):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        
        supabase = create_client(url, key)
        
        # check the user id in auth)userID is an employer
        
        check_user = supabase.table("employee").select("user_id").eq("user_id", auth_userID).single().execute()
        
        if check_user.data and check_user.data["user_id"] == auth_userID:
            apply_job = supabase.table("employee_history").update({"applied": True}).eq("job_id", job_id).eq("user_id", auth_userID).execute()
            
            if apply_job.data:
                return{
                    "Status": "Successfull",
                    "Message": f"You applied to job {job_id}"
                }
            else:
                return {
                    "Status": "Error",
                    "Message": "Error/Failed in applying"
                }
        else:
            return {
                "Status": "Error",
                "Message": "Can't find the user"
            }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Server Error",
            "Details": f"{e}"
        }

# view all apllicants of a job listing
@app.get("/job/{job_id}/applicants")
async def viewAllApplicantsInJobListing(request: Request, job_id: str):
    try:
        auth_userID = await getAuthUserIdFromRequest(redis, request)
        
        supabase = create_client(url, key)
        
        check_user = supabase.table("employers").select("user_id").eq("user_id", auth_userID).single().execute()
        
        if check_user.data and check_user.data["user_id"] == auth_userID:
            get_all_applicants = supabase.table("employee_history").select("*").eq("job_id", job_id).eq("applied", True).execute()
            
            if get_all_applicants.data:
                return {
                    "Status": "Successfull",
                    "Applicants": get_all_applicants.data
                }
            else:
                return {
                    "Status": "Successfull",
                    "Message": "No Applicants"
                }
        else:
            return {
                "Status": "Error",
                "Message": "User not Found"
            }
    except Exception as e:
        return {
            "Status": "Error",
            "Message": "Internal Server Error",
            "Details": f"{e}"
        }