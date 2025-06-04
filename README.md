# PWDE-JOB MAIN API
A job board platform specifically designed for People with Disabilities (PWD)

## Overview
PWDE-JOB is a specialized job board platform that connects employers with qualified PWD candidates. The platform provides a comprehensive suite of features for both job seekers and employers, with a focus on accessibility and inclusivity.

**Click the badge to see api docuemantion**
(or check it yourself its in the docs folder)

[![Docs](https://img.shields.io/badge/docs-GitBook-brightgreen)](https://my-docuemnations.gitbook.io/pwde-job-api-documentation#authentication-endpoints)

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

### Overall Progress: 53.85% Complete

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
- [x] Job Management System
  - Create jobs
  - View all jobs
  - View specific job
  - Delete jobs
  - Update jobs

### In Progress
- [ ] Job recommendation engine 
- [ ] Advanced profile management system
  - Resume upload
  - Skills management
  - Experience tracking
- [ ] Notification system
- [ ] Messaging system
- [ ] Employer dashboard
  - Application analytics
  - Candidate insights
  - Performance metrics
- [ ] Zoom integration
- [ ] Resume screening system

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

## Areas for Improvement

### Authentication System
1. Fix employer login session storage - currently using wrong key format
2. Add password requirements (minimum length, special characters, etc.)
3. Add email verification system
4. Add "Forgot Password" feature
5. Add session timeout and auto-logout

### Job Management
1. Fix job creation endpoint - currently using GET instead of POST
2. Add required field validation for job posts
3. Add pagination for job listings (show 10 jobs per page)
4. Add search and filter options for jobs
5. Add job application system
6. Add job status (open/closed/filled)

### Profile Management
1. Add profile update feature
2. Add profile picture upload
3. Add resume upload system
4. Fix skills storage - currently stored as text, should be proper list
5. Add experience and education sections

### Security
1. Add rate limiting to prevent spam
2. Add input validation to prevent bad data
3. Improve error messages
4. Add proper session management
5. Add API key validation

### API Structure
1. Make response formats consistent
2. Add API versioning (v1, v2, etc.)
3. Add proper error codes
4. Add request validation
5. Add API documentation

### Performance
1. Add caching for frequently accessed data
2. Optimize database queries
3. Add database indexes
4. Add request timeout handling
5. Add connection pooling

### User Experience
1. Add better error messages
2. Add loading states
3. Add success notifications
4. Add form validation
5. Add auto-save for forms

### Testing
1. Add unit tests
2. Add integration tests
3. Add API tests
4. Add security tests
5. Add performance tests

### Documentation
1. Add API usage examples
2. Add setup instructions
3. Add deployment guide
4. Add troubleshooting guide
5. Add contribution guidelines

veiw

