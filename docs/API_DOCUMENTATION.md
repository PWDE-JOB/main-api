# PWDE-JOB API Documentation (Updated)

## Table of Contents
1. [General Endpoints](#general-endpoints)
2. [Employee Endpoints](#employee-endpoints)
3. [Employer Endpoints](#employer-endpoints)
4. [Error Handling](#error-handling)
5. [Frontend Implementation Tips](#frontend-implementation-tips)

---

## General Endpoints

### Authentication

#### Employee Signup
- **Endpoint**: `POST /signupEmployee`
- **Description**: Register a new employee account. Supports all profile fields and file uploads in a single step. Uses `multipart/form-data`.
- **Request (multipart/form-data)**:
  - `full_name` (string, required)
  - `email` (string, required)
  - `password` (string, required)
  - `address` (string, optional)
  - `phone_number` (string, optional)
  - `short_bio` (string, optional)
  - `disability` (string, optional)
  - `skills` (string, optional, comma-separated or JSON array)
  - `resume` (file, optional, PDF only, max 5MB)
  - `profile_pic` (file, optional, JPG/JPEG/PNG/GIF, max 5MB)
  - `pwd_id_front` (file, optional, image)
  - `pwd_id_back` (file, optional, image)

- **Sample Request (curl)**:
```bash
curl -X POST "http://your-api-url/signupEmployee" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "full_name=Richard Gomex" \
  -F "email=rarara12@gmail.com" \
  -F "password=12345678" \
  -F "address=Quezon City" \
  -F "phone_number=09123456789" \
  -F "short_bio=asfdassfasfassf" \
  -F "disability=Pilay" \
  -F "skills=AWS,Figma,SEO,Python,Java" \
  -F "resume=@/path/to/resume.pdf" \
  -F "profile_pic=@/path/to/profile.jpg" \
  -F "pwd_id_front=@/path/to/pwd-front.jpg" \
  -F "pwd_id_back=@/path/to/pwd-back.jpg"
```

- **Sample Response**:
```json
{
  "Status": "Successfull",
  "Message": "Richard Gomex has been successfully signed up",
  "Details": [
    {
      "id": 24,
      "user_id": "932ffa37-61d3-41a4-b621-94d9d834e032",
      "full_name": "Richard Gomex",
      "disability": "Pilay",
      "skills": "AWS,Figma,SEO,Python,Java",
      "created_at": "2025-06-13T15:53:47.207587+00:00",
      "role": "employee",
      "resume_url": "https://.../resume_sample.pdf?",
      "profile_pic_url": "https://.../77.jpg?",
      "address": "Quezon City",
      "phone_number": "09123456789",
      "short_bio": "asfdassfasfassf",
      "pwd_id_front_url": "https://.../pwdidfront/...",
      "pwd_id_back_url": "https://.../pwdidback/...",
      "email": "rarara12@gmail.com"
    }
  ]
}
```

- **Tips for React Native (Employee Frontend):**
  - Use `FormData` to build the request.
  - Use `expo-image-picker` for images and `expo-document-picker` for PDFs.
  - Example:
    ```javascript
    const formData = new FormData();
    formData.append('full_name', 'Richard Gomex');
    // ...other fields
    formData.append('resume', { uri: resume.uri, type: 'application/pdf', name: resume.name });
    formData.append('profile_pic', { uri: profilePic.uri, type: 'image/jpeg', name: 'profile.jpg' });
    await fetch('http://your-api-url/signupEmployee', { method: 'POST', body: formData });
    ```
  - Always check file size and type before upload.
  - Omit fields you don't want to set.

---

#### Employer Signup
- **Endpoint**: `POST /signupEmployer`
- **Description**: Register a new employer account. Supports company logo upload. Uses `multipart/form-data`.
- **Request (multipart/form-data)**:
  - `email` (string, required)
  - `password` (string, required)
  - `company_name` (string, required)
  - `company_level` (string, required)
  - `website_url` (string, required)
  - `company_type` (string, required)
  - `industry` (string, required)
  - `admin_name` (string, required)
  - `description` (string, required)
  - `location` (string, required)
  - `tags` (string, required)
  - `file` (file, required, JPG/JPEG/PNG/GIF, max 5MB)

- **Sample Request (curl)**:
```bash
curl -X POST "http://your-api-url/signupEmployer" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "email=test12@gmail.com" \
  -F "password=your_secure_password" \
  -F "company_name=BlaBla Inc." \
  -F "company_level=Medium" \
  -F "website_url=blbla.com" \
  -F "company_type=LLC" \
  -F "industry=Technology" \
  -F "admin_name=John Stuart" \
  -F "description=agsdfhgashjkfghjas" \
  -F "location=London" \
  -F "tags=hiring" \
  -F "file=@/path/to/your/logo.jpg"
```

- **Sample Response**:
```json
{
  "Status": "Successfull",
  "Message": "BlaBla Inc. has been successfully signed up",
  "Details": "data=[{...employer fields..., 'logo_url': 'https://.../companylogo/...'}] count=None"
}
```

- **Tips for Web Frontend (Employer):**
  - Use a standard HTML `<form>` with `enctype="multipart/form-data"` or use `FormData` in JavaScript.
  - Example with Axios:
    ```javascript
    const formData = new FormData();
    formData.append('email', 'test12@gmail.com');
    // ...other fields
    formData.append('file', logoFile);
    await axios.post('http://your-api-url/signupEmployer', formData, { headers: { 'Content-Type': 'multipart/form-data' } });
    ```
  - Validate file type and size before upload.
  - Omit fields you don't want to set.

---

### Profile Management

#### Update Employee Profile
- **Endpoint**: `POST /update-profile/employee`
- **Description**: Update an employee's profile information. All fields except PWD ID Front and PWD ID Back can be updated. Resume and profile picture can be uploaded. Only non-empty fields are updated; omitted or empty fields are ignored and not overwritten.
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request (multipart/form-data)**:
  - `full_name` (string, optional)
  - `address` (string, optional)
  - `phone_number` (string, optional)
  - `short_bio` (string, optional)
  - `disability` (string, optional)
  - `skills` (string, optional, comma-separated or JSON array)
  - `resume` (file, optional, PDF only, max 5MB)
  - `profile_pic` (file, optional, JPG/JPEG/PNG/GIF, max 5MB)

- **Sample Request (curl)**:
```bash
curl -X POST "http://your-api-url/update-profile/employee" \
  -H "Authorization: Bearer <access_token>" \
  -F "full_name=Richard Gomex" \
  -F "address=Quezon City" \
  -F "phone_number=09123456789" \
  -F "short_bio=asfdassfasfassf" \
  -F "disability=Pilay" \
  -F "skills=AWS,Figma,SEO,Python,Java" \
  -F "resume=@/path/to/resume.pdf" \
  -F "profile_pic=@/path/to/profile.jpg"
```

- **Sample Response**:
```json
{
  "Status": "Successfull",
  "Message": "Update successfull"
}
```

- **Error Responses**:
```json
{
  "Status": "Error",
  "Message": "Resume must be a PDF file"
}
{
  "Status": "Error",
  "Message": "Profile picture must be an image file (JPG, JPEG, PNG, or GIF)"
}
{
  "Status": "Error",
  "Message": "No valid fields provided for update."
}
{
  "Status": "Error",
  "Message": "A unique field value you are trying to update already exists for another employee."
}
```

- **Notes:**
  - `pwd_id_front` and `pwd_id_back` cannot be updated via this endpoint.
  - If a file is provided but is empty, it will be ignored.
  - If a field is omitted or left empty, it will not overwrite the existing value in the database.
  - Only changed fields are updated.
  - Resume must be a PDF and profile picture must be an image (JPG, JPEG, PNG, or GIF).
  - File size for uploads is limited to 5MB each.
  - **React Native Tip:** Use the same `FormData` approach as signup. Omit fields you don't want to update.

#### Update Employer Profile
- **Endpoint**: `POST /update-profile/employer`
- **Description**: Update an employer's profile information. All fields from signup can be updated, including company logo. Only non-empty fields are updated; omitted or empty fields are ignored and not overwritten.
- **Headers Required**: 
  - `Authorization: Bearer <access_token>`
- **Request (multipart/form-data)**:
  - `company_name` (string, optional)
  - `company_level` (string, optional)
  - `website_url` (string, optional)
  - `company_type` (string, optional)
  - `industry` (string, optional)
  - `admin_name` (string, optional)
  - `description` (string, optional)
  - `location` (string, optional)
  - `tags` (string, optional)
  - `logo` (file, optional, JPG/JPEG/PNG/GIF, max 5MB)

- **Sample Request (curl)**:
```bash
curl -X POST "http://your-api-url/update-profile/employer" \
  -H "Authorization: Bearer <access_token>" \
  -F "company_name=BlaBla Inc." \
  -F "company_level=Medium" \
  -F "website_url=blbla.com" \
  -F "company_type=LLC" \
  -F "industry=Technology" \
  -F "admin_name=John Stuart" \
  -F "description=agsdfhgashjkfghjas" \
  -F "location=London" \
  -F "tags=hiring" \
  -F "logo=@/path/to/logo.jpg"
```

- **Sample Response**:
```json
{
  "Status": "Successfull",
  "Message": "Update successfull"
}
```

- **Error Responses**:
```json
{
  "Status": "Error",
  "Message": "Invalid logo file type. Allowed: JPG, JPEG, PNG, GIF"
}
{
  "Status": "Error",
  "Message": "Logo file size must be less than 5MB"
}
{
  "Status": "Error",
  "Message": "No valid fields provided for update."
}
{
  "Status": "Error",
  "Message": "A unique field value you are trying to update already exists for another employer."
}
```

- **Notes:**
  - If a file is provided but is empty, it will be ignored.
  - If a field is omitted or left empty, it will not overwrite the existing value in the database.
  - Only changed fields are updated.
  - Logo must be an image (JPG, JPEG, PNG, or GIF), max 5MB.
  - **Web Tip:** Use `FormData` in JavaScript or a proper HTML form. Omit fields you don't want to update.

---

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
5. Unique constraint violations (duplicate values)
6. File validation errors (type/size)

---

## Frontend Implementation Tips

### For Employers (Web)
- Use `FormData` for all endpoints that require file uploads.
- Validate file types and sizes before sending.
- Omit fields you don't want to update; only non-empty fields are updated.
- Use Axios or Fetch for API calls. Example:
  ```javascript
  const formData = new FormData();
  formData.append('company_name', 'BlaBla Inc.');
  // ...other fields
  if (logoFile) formData.append('logo', logoFile);
  await axios.post('http://your-api-url/update-profile/employer', formData, { headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'multipart/form-data' } });
  ```
- Handle error responses and show user-friendly messages.

### For Employees (React Native)
- Use `FormData` and `fetch` or `axios` for all endpoints with file uploads.
- Use `expo-image-picker` for images and `expo-document-picker` for PDFs.
- Omit fields you don't want to update; only non-empty fields are updated.
- Example:
  ```javascript
  const formData = new FormData();
  formData.append('full_name', 'Richard Gomex');
  // ...other fields
  if (resume) formData.append('resume', { uri: resume.uri, type: 'application/pdf', name: resume.name });
  if (profilePic) formData.append('profile_pic', { uri: profilePic.uri, type: 'image/jpeg', name: 'profile.jpg' });
  await fetch('http://your-api-url/update-profile/employee', { method: 'POST', headers: { 'Authorization': `Bearer ${token}` }, body: formData });
  ```
- Always check file size and type before upload.
- Handle error responses and show user-friendly messages.

---

## Additional Notes
- All endpoints requiring authentication must include the `Authorization: Bearer <access_token>` header.
- For all file uploads, use `multipart/form-data`.
- For updates, only non-empty fields are updated; omitted or empty fields are ignored.
- For signup, all required fields must be provided.
- For best UX, always provide feedback to users on success or error.
