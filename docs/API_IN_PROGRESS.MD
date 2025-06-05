### 1️ Profile Update Endpoint - DONE
- **Purpose**: Allow users (employees and employers) to update their profile information (name, contact info, skills, experience, profile picture).
- **Example**:  
  `POST /update-profile/{auth_userID}`
---

### 2️ Resume Upload Endpoint
- **Purpose**: Enable employees to upload, update, or delete their resumes.
- **Example**:  
  `POST /upload-resume/{auth_userID}`

---

### 3️ Job Application Endpoint - done
- **Purpose**: Allow employees to apply for jobs and track their applications.
- **Example**:  
  `POST /apply-job/{job_id}`

---

### 4️ Job Application History Endpoint
- **Purpose**: Let employees view the list and status of jobs they have applied to.
- **Example**:  
  `GET /application-history/{auth_userID}`

---

### 6️ Job Recommendation Endpoint -DONE
- **Purpose**: Provide personalized job recommendations to employees based on their profile and skills.
- **Example**:  
  `GET /recommend-jobs/{auth_userID}`

---

### 7️ Notification Endpoints
- **Purpose**:  
  - **Send notifications**: For job matches, application status, interview invites, etc.  
  - **View notifications**: List all notifications for a user.
- **Examples**:  
  - `POST /send-notification`  
  - `GET /notifications/{auth_userID}`

---

### 8️ Messaging Endpoints
- **Purpose**: Enable direct messaging between employees and employers.
- **Examples**:  
  - `POST /send-message`  
  - `GET /messages/{conversation_id}`

---

### 9️ Employer Dashboard Endpoints
- **Purpose**: View analytics, application statistics, and candidate insights.
- **Examples**:  
  - `GET /dashboard/analytics/{employer_id}`  
  - `GET /dashboard/applications/{employer_id}`

---

### 10 Job Management Endpoints -donne
- **Purpose**: Allow employers to create, update, delete, and manage job postings.
- **Examples**:  
  - `POST /create-job`  
  - `PUT /update-job/{job_id}`  
  - `DELETE /delete-job/{job_id}`  
  - `GET /jobs/{employer_id}`

---

### 1️1️ Assessment/Test Endpoints
- **Purpose**: Employers can send assessments to candidates and review results.
- **Examples**:  
  - `POST /send-assessment`  
  - `GET /assessment-results/{candidate_id}`

---

### 1️2️ Zoom Integration Endpoints
- **Purpose**: Schedule and manage video interviews.
- **Examples**:  
  - `POST /schedule-zoom-interview`  
  - `GET /zoom-meetings/{user_id}`

---

### 1️3️ Resume Screening Endpoint
- **Purpose**: Automatically screen and rank resumes for employers.
- **Example**:  
  `POST /screen-resume/{job_id}`

---

### 1️5️ Password Reset & Email Verification Endpoints
- **Purpose**: Allow users to reset their password and verify their email.
- **Examples**:  
  - `POST /request-password-reset`  
  - `POST /reset-password`  
  - `POST /verify-email`

---

### 1️6️ Admin/Moderation Endpoints
- **Purpose**: For admin users to manage users, jobs, and platform content.
- **Examples**:  
  - `GET /admin/users`  
  - `DELETE /admin/delete-user/{user_id}`

---
### 1️7️ View Applicants for a Job Endpoint - Done
- **Purpose**: Allow employers to view all applicants for a specific job listing.
- **Example**:  
  `GET /jobs/{job_id}/applicants`

---

### 1️8️ Logout Endpoint 
- **Purpose**: Allow users to securely logout by deleting their session or token.
- **Example**:  
  `POST /logout`