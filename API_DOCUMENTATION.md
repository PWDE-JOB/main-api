# PWDE-JOB API Documentation

## Authentication Endpoints

### Employee Signup
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
- **Frontend Usage Example**:
  ```javascript
  const signupEmployee = async (employeeData) => {
    try {
      const response = await fetch('http://localhost:8000/signupEmployee', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(employeeData)
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error signing up employee:', error);
      throw error;
    }
  };
  ```

### Employer Signup
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
- **Frontend Usage Example**:
  ```javascript
  const signupEmployer = async (employerData) => {
    try {
      const response = await fetch('http://localhost:8000/signupEmployer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(employerData)
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error signing up employer:', error);
      throw error;
    }
  };
  ```

### Employee Login
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
- **Frontend Usage Example**:
  ```javascript
  const loginEmployee = async (credentials) => {
    try {
      const response = await fetch('http://localhost:8000/login-employee', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials)
      });
      const data = await response.json();
      if (data.Status === "Success") {
        // Store the user ID in localStorage or state management
        localStorage.setItem('userId', data['App User ID']);
      }
      return data;
    } catch (error) {
      console.error('Error logging in:', error);
      throw error;
    }
  };
  ```

### Employer Login
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
- **Frontend Usage Example**:
  ```javascript
  const loginEmployer = async (credentials) => {
    try {
      const response = await fetch('http://localhost:8000/login-employer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials)
      });
      const data = await response.json();
      if (data.Status === "Success") {
        // Store the user ID in localStorage or state management
        localStorage.setItem('userId', data['App User ID']);
      }
      return data;
    } catch (error) {
      console.error('Error logging in:', error);
      throw error;
    }
  };
  ```

## Profile Management

### View Profile
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
- **Frontend Usage Example**:
  ```javascript
  const viewProfile = async () => {
    try {
      const accessToken = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/view-profile', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching profile:', error);
      throw error;
    }
  };
  ```

## Job Management

### Create Job
- **Endpoint**: `POST /create-jobs`
- **Description**: Create a new job listing
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "title": "Software Developer",
    "description": "Looking for a skilled developer",
    "skill_1": "Python",
    "skill_2": "JavaScript",
    "skill_3": "React",
    "skill_4": "Node.js",
    "skill_5": "SQL",
    "pwd_friendly": true
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Sucessfull",
    "Message": "Job has been created",
    "Details": "data=[{'id': 8, 'user_id': '148cc1c6-2e81-4037-913c-7617564baa33', 'title': 'Software Developer', 'job_description': 'Looking for a skilled developer', 'skill_1': 'Python', 'skill_2': 'JavaScript', 'skill_3': 'React', 'skill_4': 'Node.js', 'skill_5': 'SQL', 'pwd_friendly': true, 'created_at': '2025-06-04T06:23:51.104274+00:00'}] count=None"
  }
  ```
- **Frontend Usage Example**:
  ```javascript
  const createJob = async (jobData) => {
    try {
      const accessToken = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/create-jobs', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify(jobData)
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error creating job:', error);
      throw error;
    }
  };
  ```

### View All Jobs
- **Endpoint**: `GET /view-all-jobs`
- **Description**: Retrieve all jobs created by the authenticated employer
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "jobs": [
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
- **Frontend Usage Example**:
  ```javascript
  const viewAllJobs = async () => {
    try {
      const accessToken = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:8000/view-all-jobs', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });
      const data = await response.json();
      return data.jobs;
    } catch (error) {
      console.error('Error fetching jobs:', error);
      throw error;
    }
  };
  ```

### View Specific Job
- **Endpoint**: `GET /view-job/{id}`
- **Description**: Retrieve details of a specific job
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Job Number 8 Found",
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
- **Frontend Usage Example**:
  ```javascript
  const viewJob = async (jobId) => {
    try {
      const accessToken = localStorage.getItem('access_token');
      const response = await fetch(`http://localhost:8000/view-job/${jobId}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching job:', error);
      throw error;
    }
  };
  ```

### Delete Job
- **Endpoint**: `POST /delete-job/{id}`
- **Description**: Delete a specific job listing
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Job 9 deleted successfully"
  }
  ```
- **Frontend Usage Example**:
  ```javascript
  const deleteJob = async (jobId) => {
    try {
      const accessToken = localStorage.getItem('access_token');
      const response = await fetch(`http://localhost:8000/delete-job/${jobId}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error deleting job:', error);
      throw error;
    }
  };
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

## Versioning

The current API version is v1. All endpoints are prefixed with `/v1/` (e.g., `/v1/signupEmployee`). 