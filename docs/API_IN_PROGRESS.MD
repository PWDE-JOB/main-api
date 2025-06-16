### 1️ Profile Update Endpoint - DONE
- **Purpose**: Allow users (employees and employers) to update their profile information (name, contact info, skills, experience, profile picture).
- **Example**:  
  `POST /update-profile/{auth_userID}`
---

### 2️ Resume Upload Endpoint - IN PROGRESS
- **Purpose**: Enable employees to upload, update, or delete their resumes.
- **Example**:  
  `POST /upload-resume`
- **Features**:
  - PDF file upload
  - Text extraction
  - Resume storage
  - File validation

---

### 3️ Job Application Endpoint - DONE
- **Purpose**: Allow employees to apply for jobs and track their applications.
- **Example**:  
  `POST /apply-job/{job_id}`

---

### 4️ Job Application History Endpoint - DONE
- **Purpose**: Let employees view the list and status of jobs they have applied to.
- **Example**:  
  `GET /application-history/{auth_userID}`

---

### 5️ Job Recommendation Endpoint - DONE
- **Purpose**: Provide personalized job recommendations to employees based on their profile and skills.
- **Example**:  
  `GET /recommend-jobs/{auth_userID}`

---

### 6️ Job Management Endpoints - DONE
- **Purpose**: Allow employers to create, update, delete, and manage job postings.
- **Examples**:  
  - `POST /create-job`  
  - `PUT /update-job/{job_id}`  
  - `DELETE /delete-job/{job_id}`  
  - `GET /jobs/{employer_id}`

---

### 7️ View Applicants for a Job Endpoint - DONE
- **Purpose**: Allow employers to view all applicants for a specific job listing.
- **Example**:  
  `GET /jobs/{job_id}/applicants`

---

### 8️ Logout Endpoint - DONE
- **Purpose**: Allow users to securely logout by deleting their session or token.
- **Example**:  
  `POST /logout`

---

### 9️ Resume Screening Endpoint - IN PROGRESS
- **Purpose**: Enable employers to screen and evaluate resumes
- **Example**:  
  `POST /screen-resume/{resume_id}`
- **Features**:
  - Text analysis
  - Skill matching
  - Experience detection
  - Education level detection
  - Match scoring

---

### 10️ Application Status Management - IN PROGRESS
- **Purpose**: Track and update application statuses
- **Example**:  
  `PUT /application/{application_id}/status`
- **Features**:
  - Status updates (pending, reviewed, accepted, rejected)
  - Status history
  - Notification triggers

---

### Third-Party Integrations (No API Endpoints Needed)

#### Assessment System
- **Implementation**: Google Forms or similar third-party form service
- **Purpose**: Employers can create and send assessments to candidates
- **Note**: No need for custom API endpoints as these services provide their own APIs

#### Messaging System
- **Implementation**: Supabase Realtime or similar service
- **Purpose**: Enable direct messaging between employees and employers
- **Note**: Use Supabase's built-in realtime features instead of custom endpoints

#### Notification System
- **Implementation**: Supabase Realtime or similar service
- **Purpose**: Send notifications for job matches, application status, etc.
- **Note**: Use Supabase's built-in notification features

#### Video Interview System
- **Implementation**: Zoom, Google Meet, or similar service
- **Purpose**: Schedule and manage video interviews
- **Note**: Use the service's own API directly from the frontend

---

### Removed Endpoints (Not Needed)
- ~~Notification Endpoints~~ (Using Supabase Realtime)
- ~~Messaging Endpoints~~ (Using Supabase Realtime)
- ~~Zoom Integration Endpoints~~ (Using Zoom API directly)
- ~~Assessment/Test Endpoints~~ (Using Google Forms or similar)
- ~~Admin/Moderation Endpoints~~ (Can be handled through Supabase dashboard)