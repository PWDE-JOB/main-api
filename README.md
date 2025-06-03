# PWDE-JOB MAIN API
A job board platform specifically designed for People with Disabilities (PWD)

## Overview
PWDE-JOB is a specialized job board platform that connects employers with qualified PWD candidates. The platform provides a comprehensive suite of features for both job seekers and employers, with a focus on accessibility and inclusivity.

## Features

### Job Seeker Features
- **Authentication**
  - Secure login and registration system
  - Profile management
  - Password recovery

- **Job Recommendations**
  - Personalized job matching
  - Skill-based recommendations
  - Location-based filtering

- **Profile Management**
  - Professional profile creation
  - Resume upload and management
  - Skills and experience tracking

- **Notifications**
  - Job application updates
  - New job matches
  - Interview invitations
  - System notifications

- **Application History**
  - Track job applications
  - View application status
  - Save favorite jobs

- **Settings**
  - Account preferences
  - Notification settings
  - Privacy controls

- **Messaging System**
  - Direct communication with employers
  - Interview scheduling
  - Application follow-ups

### Employer Features
- **Authentication**
  - Company account management
  - Admin access control

- **Job Listing Statistics**
  - Application analytics
  - Candidate insights
  - Performance metrics

- **Job Listings Management**
  - Create new job postings
  - Update existing listings
  - Delete expired positions
  - Draft management

- **Initial Test Management**
  - Create assessment tests
  - Review test results
  - Candidate evaluation

- **Messaging System**
  - Candidate communication
  - Interview coordination
  - Application feedback

### Integrations
- **Zoom Integration**
  - Video interview scheduling
  - Meeting management
  - Recording capabilities

- **Resume Screening**
  - Automated resume parsing
  - Skill matching
  - Candidate ranking

## Progress Tracking

### Overall Progress: 46.15% Complete

### Completed
- [x] Project initialization
- [x] Basic project structure
- [x] Authentication system
  - Employee signup
  - Employer signup
  - Employee login
  - Employer login
- [x] Database schema design
- [x] API endpoints planning
- [x] Basic profile management
  - Profile viewing

### In Progress
- [ ] Job recommendation engine
- [ ] Advanced profile management system
- [ ] Notification system
- [ ] Messaging system
- [ ] Employer dashboard
- [ ] Zoom integration
- [ ] Resume screening system

## API Documentation

### Authentication Endpoints

#### Employee Signup
- **Endpoint**: `POST /signupEmployee`
- **Description**: Register a new employee account
- **Request Body**:
  ```json
  {
    "first_name": "string",
    "middle_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string",
    "disability": "string",
    "skills": ["string"]
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "Testing Name has been successfully signed up",
    "Details": "data=[{'id': 20, 'user_id': '111111-111111-111111-11111-111111111', 'first_name': 'Testing Name', 'middle_name': 'Cruz', 'last_name': 'string', 'disability': 'Pilay', 'skills': \"['SEO', 'Typing', 'Figma']\", 'created_at': '2025-06-03T08:15:38.142711+00:00', 'role': 'employee'}] count=None"
  }
  ```

#### Employer Signup
- **Endpoint**: `POST /signupEmployer`
- **Description**: Register a new employer account
- **Request Body**:
  ```json
  {
    "first_name": "string",
    "middle_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Sample Response**:
  ```json
  {
    "Status": "Successfull",
    "Message": "John has been successfully signed up",
    "Details": "data=[{'user_id': '111111-111111-111111-11111-111111111', 'first_name': 'John', 'middle_name': 'Dela', 'last_name': 'Crixx', 'email': 'rarara12@gmail.com', 'role': 'employer', 'created_at': '2025-06-03T08:16:25.221844+00:00', 'id': 3}] count=None"
  }
  ```

#### Employee Login
- **Endpoint**: `POST /login-employee`
- **Description**: Authenticate an employee user
- **Note**: The `auth_userID` returned in the response needs to be stored on the client side (frontend) as it will be required for subsequent API calls to other endpoints.
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Login successful. Session stored in Redis.",
    "App User ID": "111111-111111-111111-11111-111111111",
    "Debug Session Key": "session:111111-111111-111111-11111-111111111",
    "Stored User ID": "111111-111111-111111-11111-111111111"
  }
  ```

#### Employer Login
- **Endpoint**: `POST /login-employer`
- **Description**: Authenticate an employer user
- **Note**: The `auth_userID` returned in the response needs to be stored on the client side (frontend) as it will be required for subsequent API calls to other endpoints.
- **Sample Response**:
  ```json
  {
    "Status": "Success",
    "Message": "Login successful. Session stored in Redis.",
    "App User ID": "111111-111111-111111-11111-111111111",
    "Debug Session Key": "session:111111-111111-111111-11111-111111111",
    "Stored User ID": "111111-111111-111111-11111-111111111"
  }
  ```

### Profile Management

#### View Profile
- **Endpoint**: `GET /view-profile/{auth_userID}`
- **Description**: Retrieve user profile information
- **Sample Response**:
  ```json
  {
    "Profile": {
      "user_id": "111111-111111-111111-11111-111111111",
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

## Technical Stack
- Backend: Python
- Database: Supabase (Postgresql)
- API: Fastapi
- Authentication: Supabase

## Getting Started
(To be added)

## Contributing
(To be added)

## License
(To be added)

## Contact
(To be added)

veiw

