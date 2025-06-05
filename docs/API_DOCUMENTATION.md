# PWDE-JOB API Documentation

## Table of Contents
1. [General Endpoints](#general-endpoints)
2. [Employee Endpoints](#employee-endpoints)
3. [Employer Endpoints](#employer-endpoints)
4. [Error Handling](#error-handling)
5. [Best Practices](#best-practices)
6. [Frontend Implementation Examples](#frontend-implementation-examples)

## General Endpoints

### Authentication

#### Employee Signup
- **Endpoint**: `POST /signupEmployee`
- **Description**: Register a new employee account with disability information and skills
- **Request Body**:
  ```json
  {
    "first_name": "Testing Name",
    "middle_name": "Cruz",
    "last_name": "string",
    "email": "test12@gmail.com",
    "password": "1122334455",
    "disability": "Pilay",
    "skills": ["SEO", "Typing", "Figma"]
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Testing Name has been successfully signed up",
    "Details": "data=[{'id': 20, 'user_id': 'f9b86db6-93dc-4e29-a1be-6dfcb114b8f7', 'first_name': 'Testing Name', 'middle_name': 'Cruz', 'last_name': 'string', 'disability': 'Pilay', 'skills': \"['SEO', 'Typing', 'Figma']\", 'created_at': '2025-06-03T08:15:38.142711+00:00', 'role': 'employee'}] count=None"
  }
  ```

#### Employer Signup
- **Endpoint**: `POST /signupEmployer`
- **Description**: Register a new employer account
- **Request Body**:
  ```json
  {
    "first_name": "John",
    "middle_name": "Dela",
    "last_name": "Crixx",
    "email": "rarara12@gmail.com",
    "password": "1122334455"
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "John has been successfully signed up",
    "Details": "data=[{'user_id': '148cc1c6-2e81-4037-913c-7617564baa33', 'first_name': 'John', 'middle_name': 'Dela', 'last_name': 'Crixx', 'email': 'rarara12@gmail.com', 'role': 'employer', 'created_at': '2025-06-03T08:16:25.221844+00:00', 'id': 3}] count=None"
  }
  ```

#### Employee Login
- **Endpoint**: `POST /login-employee`
- **Description**: Authenticate an employee user and create a session
- **Request Body**:
  ```json
  {
    "email": "test12@gmail.com",
    "password": "1122334455"
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Login successful. Session stored in Redis.",
    "App User ID": "f9b86db6-93dc-4e29-a1be-6dfcb114b8f7",
    "Debug Session Key": "session:f9b86db6-93dc-4e29-a1be-6dfcb114b8f7",
    "Stored User ID": "f9b86db6-93dc-4e29-a1be-6dfcb114b8f7"
  }
  ```

#### Employer Login
- **Endpoint**: `POST /login-employer`
- **Description**: Authenticate an employer user and create a session
- **Request Body**:
  ```json
  {
    "email": "rarara12@gmail.com",
    "password": "1122334455"
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Login successful. Session stored in Redis.",
    "App User ID": "148cc1c6-2e81-4037-913c-7617564baa33",
    "Debug Session Key": "session:148cc1c6-2e81-4037-913c-7617564baa33",
    "Stored User ID": "148cc1c6-2e81-4037-913c-7617564baa33"
  }
  ```

#### View Profile
- **Endpoint**: `GET /view-profile`
- **Description**: Retrieve user profile information
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Profile": {
      "user_id": "148cc1c6-2e81-4037-913c-7617564baa33",
      "first_name": "John",
      "middle_name": "Dela",
      "last_name": "Crixx",
      "email": "rarara12@gmail.com",
      "role": "employer",
      "created_at": "2025-06-03T08:16:25.221844+00:00",
      "id": 3
    }
  }
  ```

#### Logout
- **Endpoint**: `POST /logout`
- **Description**: Log out the current user by invalidating their session token
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Successfully logged out"
  }
  ```
- **Error Response**:
  ```json
  {
    "Status": "ERROR",
    "Message": "Logout failed",
    "Details": "Error details here"
  }
  ```

### Profile Management

#### Update Employee Profile
- **Endpoint**: `POST /update-profile/employee`
- **Description**: Update an employee's profile information including name, disability, and skills
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "first_name": "Updated Name",
    "middle_name": "Updated Middle",
    "last_name": "Updated Last",
    "disability": "Updated Disability",
    "skills": ["Updated Skill 1", "Updated Skill 2"]
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Update successfull"
  }
  ```

#### Update Employer Profile
- **Endpoint**: `POST /update-profile/employer`
- **Description**: Update an employer's profile information
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "first_name": "Updated Name",
    "middle_name": "Updated Middle",
    "last_name": "Updated Last"
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Update successfull"
  }
  ```

## Employee Endpoints

### Job Application

#### Apply for Job
- **Endpoint**: `POST /apply-job/{job_id}`
- **Description**: Apply for a specific job
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Successfully applied for job",
    "Details": {
      "id": 1,
      "user_id": "f9b86db6-93dc-4e29-a1be-6dfcb114b8f7",
      "job_id": 16,
      "applied": true,
      "created_at": "2025-06-05T14:13:35.947101+00:00"
    }
  }
  ```

#### Get Job Recommendations
- **Endpoint**: `GET /reco-jobs`
- **Description**: Get personalized job recommendations based on skills
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "recommendations": [
      {
        "id": 13,
        "title": "Transcriptionist",
        "job_description": "aaaaaaaaaaa",
        "skill_1": "Grammar",
        "skill_2": "Transcription Tools",
        "skill_3": "Listening",
        "skill_4": "Detail Orientation",
        "skill_5": "Typing",
        "pwd_friendly": false,
        "created_at": "2025-06-05T12:57:47.917283+00:00",
        "salary": 434,
        "skill_match_score": 0.6,
        "matched_skills": [
          "typing",
          "listening",
          "grammar"
        ]
      }
    ]
  }
  ```

## Employer Endpoints

### Job Management

#### Create Job
- **Endpoint**: `POST /create-jobs`
- **Description**: Create a new job listing
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "title": "Content Writer",
    "description": "Looking for a skilled content writer",
    "skill_1": "SEO",
    "skill_2": "Copywriting",
    "skill_3": "Grammar",
    "skill_4": "WordPress",
    "skill_5": "Research",
    "pwd_friendly": true,
    "salary": 7700
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Sucessfull",
    "Message": "Job has been created",
    "Details": "data=[{'id': 11, 'user_id': '148cc1c6-2e81-4037-913c-7617564baa33', 'title': 'Content Writer', 'job_description': 'Looking for a skilled content writer', 'skill_1': 'SEO', 'skill_2': 'Copywriting', 'skill_3': 'Grammar', 'skill_4': 'WordPress', 'skill_5': 'Research', 'pwd_friendly': true, 'created_at': '2025-06-05T12:39:57.008087+00:00', 'salary': 7700}] count=None"
  }
  ```

#### View All Jobs
- **Endpoint**: `GET /view-all-jobs`
- **Description**: Retrieve all jobs created by the authenticated employer
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "jobs": [
      {
        "id": 11,
        "user_id": "148cc1c6-2e81-4037-913c-7617564baa33",
        "title": "Content Writer",
        "job_description": "Looking for a skilled content writer",
        "skill_1": "SEO",
        "skill_2": "Copywriting",
        "skill_3": "Grammar",
        "skill_4": "WordPress",
        "skill_5": "Research",
        "pwd_friendly": true,
        "created_at": "2025-06-05T12:39:57.008087+00:00",
        "salary": 7700
      }
    ]
  }
  ```

#### View Job Applicants
- **Endpoint**: `GET /job/{job_id}/applicants`
- **Description**: View all applicants for a specific job
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Applicants": [
      {
        "id": 1,
        "user_id": "f9b86db6-93dc-4e29-a1be-6dfcb114b8f7",
        "job_id": 16,
        "applied": true,
        "created_at": "2025-06-05T14:13:35.947101+00:00"
      }
    ]
  }
  ```

#### View Specific Job
- **Endpoint**: `GET /view-job/{id}`
- **Description**: Retrieve details of a specific job listing
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Job Number {id} Found",
    "Details": [
      {
        "id": 8,
        "user_id": "148cc1c6-2e81-4037-913c-7617564baa33",
        "title": "Software Developer",
        "job_description": "Looking for a skilled developer",
        "skill_1": "Python",
        "skill_2": "JavaScript",
        "skill_3": "React",
        "skill_4": "Node.js",
        "skill_5": "SQL",
        "pwd_friendly": true,
        "created_at": "2025-06-04T06:23:51.104274+00:00"
      }
    ]
  }
  ```

#### Delete Job
- **Endpoint**: `POST /delete-job/{id}`
- **Description**: Delete a specific job listing
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Job {id} deleted successfully"
  }
  ```

#### Update Job
- **Endpoint**: `POST /update-job/{id}`
- **Description**: Update an existing job listing
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "title": "Updated Job Title",
    "description": "Updated job description",
    "skill_1": "Updated Skill 1",
    "skill_2": "Updated Skill 2",
    "skill_3": "Updated Skill 3",
    "skill_4": "Updated Skill 4",
    "skill_5": "Updated Skill 5",
    "pwd_friendly": true,
    "salary": 8000
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Update successfull"
  }
  ```

## Error Handling

All endpoints follow a consistent error response format:
```json
{
  "Status": "ERROR",
  "Message": "Error message here",
  "Details": "Detailed error information (if available)"
}
```

Common error scenarios:
1. Authentication failures
2. Invalid input data
3. Resource not found
4. Server errors

## Best Practices for Frontend Implementation

1. **Authentication Flow**:
   - Store the access token securely (localStorage or secure cookie)
   - Include the token in all authenticated requests
   - Handle token expiration and refresh

2. **Error Handling**:
   - Implement proper error handling for all API calls
   - Show user-friendly error messages
   - Log errors for debugging

3. **Data Management**:
   - Cache frequently accessed data
   - Implement proper loading states
   - Handle data updates efficiently

4. **Security**:
   - Never store sensitive data in localStorage
   - Implement proper input validation
   - Use HTTPS for all API calls

## Rate Limiting

The API implements rate limiting to prevent abuse. Current limits:
- 100 requests per minute per IP
- 1000 requests per hour per user

## Frontend Implementation Examples

### Authentication and Token Management
```javascript
// Store token after login
const storeToken = (token) => {
    localStorage.setItem('access_token', token);
};

// Get token for requests
const getToken = () => {
    return localStorage.getItem('access_token');
};

// Create headers with authorization
const getAuthHeaders = () => {
    return {
        'Authorization': `Bearer ${getToken()}`,
        'Content-Type': 'application/json'
    };
};
```

**Let me walk you through how we handle authentication:**

When a user logs in, we need to store their access token so they can make authenticated requests. We're using localStorage here because it's simple and keeps the token available even if the user refreshes the page. Just remember, for a production app, you might want to use more secure options like HTTP-only cookies.

The `getToken` function is our way of getting the stored token whenever we need it. Having this separate function means if we ever need to change how we store tokens, we only need to update this one spot!

The `getAuthHeaders` function is super helpful - it creates the headers we need for every authenticated request. It adds both the authorization token and tells the server we're sending JSON data. This keeps our code DRY (Don't Repeat Yourself) since we don't have to write these headers in every API call.

### Simple GET Request Example
```javascript
// Example: View Profile
const viewProfile = async () => {
    try {
        const response = await fetch('http://your-api-url/view-profile', {
            method: 'GET',
            headers: getAuthHeaders()
        });
        
        const data = await response.json();
        if (data.Status === "ERROR") {
            throw new Error(data.Message);
        }
        return data;
    } catch (error) {
        console.error('Error fetching profile:', error);
        throw error;
    }
};
```

**Here's how we handle a simple GET request:**

I'm using async/await here because it makes the code much easier to read than the old promise chains. It's like writing synchronous code, but it's still non-blocking!

The try-catch block is our safety net - it catches any problems that might happen, whether it's a network error or if the API returns an error response. This way, we can handle errors gracefully instead of having the app crash.

Notice how we check for `data.Status === "ERROR"`? That's because our API always tells us if something went wrong in this format. If we see an error, we throw it so the code that called this function can handle it appropriately.

### POST Request with Request Body Example
```javascript
// Example: Create Job
const createJob = async (jobData) => {
    try {
        const response = await fetch('http://your-api-url/create-jobs', {
            method: 'POST',
            headers: getAuthHeaders(),
            body: JSON.stringify({
                title: jobData.title,
                description: jobData.description,
                skill_1: jobData.skill_1,
                skill_2: jobData.skill_2,
                skill_3: jobData.skill_3,
                skill_4: jobData.skill_4,
                skill_5: jobData.skill_5,
                pwd_friendly: jobData.pwd_friendly,
                salary: jobData.salary
            })
        });
        
        const data = await response.json();
        if (data.Status === "ERROR") {
            throw new Error(data.Message);
        }
        return data;
    } catch (error) {
        console.error('Error creating job:', error);
        throw error;
    }
};
```

**Let's talk about sending data to the server:**

When we're creating a new job, we need to send all the job details to the server. The `JSON.stringify()` part is important because fetch needs the body to be a string, not a JavaScript object.

I've structured the request body to match exactly what our API expects. This is crucial - if we send data in the wrong format, the server won't understand it!

The error handling here follows the same pattern as our GET request. Consistency is key in error handling - it makes debugging much easier when all our API calls handle errors the same way.

### PUT/POST Request with URL Parameters Example
```javascript
// Example: Update Job
const updateJob = async (jobId, updateData) => {
    try {
        const response = await fetch(`http://your-api-url/update-job/${jobId}`, {
            method: 'POST',
            headers: getAuthHeaders(),
            body: JSON.stringify(updateData)
        });
        
        const data = await response.json();
        if (data.Status === "ERROR") {
            throw new Error(data.Message);
        }
        return data;
    } catch (error) {
        console.error('Error updating job:', error);
        throw error;
    }
};
```

**Updating resources with URL parameters:**

For updating a job, we need both the job ID in the URL and the update data in the body. I'm using template literals (those backticks) to put the job ID in the URL - it's much cleaner than concatenating strings!

I've separated the `jobId` and `updateData` parameters because it makes the function more flexible. You can reuse this function for different jobs without changing the code.

### Error Handling Utility
```javascript
// Centralized error handling
const handleApiError = (error) => {
    if (error.response) {
        // Server responded with error
        console.error('API Error:', error.response.data);
        return error.response.data.Message || 'An error occurred';
    } else if (error.request) {
        // Request made but no response
        console.error('Network Error:', error.request);
        return 'Network error occurred';
    } else {
        // Other errors
        console.error('Error:', error.message);
        return error.message;
    }
};
```

**Making error handling user-friendly:**

This error handler is like a translator between our API and our users. It takes technical errors and turns them into messages that make sense to users.

It handles three different types of errors:
1. When the server responds with an error (like "invalid data")
2. When there's a network problem (like no internet)
3. Any other unexpected errors

We log the technical details for debugging but return user-friendly messages for the UI. This way, developers can debug issues while users get clear, understandable error messages.

### Usage Examples
```javascript
// Example usage in a React component
const JobManagement = () => {
    const [jobs, setJobs] = useState([]);
    const [error, setError] = useState(null);

    // Fetch all jobs
    const fetchJobs = async () => {
        try {
            const response = await fetch('http://your-api-url/view-all-jobs', {
                headers: getAuthHeaders()
            });
            const data = await response.json();
            setJobs(data.jobs);
        } catch (error) {
            setError(handleApiError(error));
        }
    };

    // Create new job
    const handleCreateJob = async (jobData) => {
        try {
            const result = await createJob(jobData);
            // Refresh jobs list
            fetchJobs();
            return result;
        } catch (error) {
            setError(handleApiError(error));
        }
    };

    return (
        <div>
            {error && <div className="error">{error}</div>}
            {/* Your component JSX */}
        </div>
    );
};
```

**Putting it all together in a React component:**

This is how you'd use these API functions in a real React component. We're using React's `useState` to keep track of our jobs and any errors that might occur.

The `fetchJobs` function gets all the jobs and updates our state. If something goes wrong, it shows the error to the user.

When creating a new job, we first try to create it, and if that succeeds, we refresh the jobs list to show the new job. This keeps our UI in sync with the server data.

### Axios Implementation (Alternative)
```javascript
import axios from 'axios';

// Create axios instance with default config
const api = axios.create({
    baseURL: 'http://your-api-url',
    timeout: 5000
});

// Add request interceptor for auth token
api.interceptors.request.use(config => {
    const token = getToken();
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

// Example using axios
const viewProfile = async () => {
    try {
        const response = await api.get('/view-profile');
        return response.data;
    } catch (error) {
        handleApiError(error);
    }
};
```

**Why you might want to use Axios instead of fetch:**

Axios is like fetch with superpowers! It automatically converts JSON for you, has better error handling, and gives you these cool things called interceptors.

The `axios.create()` part sets up a configured instance with our base URL and timeout. This means we don't have to repeat the full URL in every request.

The interceptor is really neat - it automatically adds our auth token to every request. No more manually adding headers in each API call!

The syntax is also much cleaner than fetch. Instead of writing `response.json()`, we can just use `response.data`. It's these little conveniences that make Axios popular among developers.
