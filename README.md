# 🎯 ATS (Applicant Tracking System)

## Project Overview

The ATS (Applicant Tracking System) is a web-based application that helps streamline the recruitment process by managing candidate applications, resumes, and hiring workflows. The system allows recruiters to upload resumes, analyze candidate information, track application status, and manage the recruitment process efficiently.

This project is built using Python, Flask, OpenCV, HTML, CSS, Bootstrap, and MySQL.

---

## Features

- Candidate Registration
- Resume Upload and Management
- Applicant Tracking
- Candidate Profile Management
- Resume Screening
- Recruitment Dashboard
- Search and Filter Candidates
- Application Status Tracking
- Responsive User Interface

---

## Technologies Used

- Python
- Flask
- OpenCV
- HTML5
- CSS3
- Bootstrap 5
- MySQL

---

## Project Structure

ATS-Project/

├── static/

│ ├── css/

│ ├── js/

│ └── images/

├── templates/

│ ├── index.html

│ ├── dashboard.html

│ ├── upload_resume.html

│ ├── candidate_list.html

│ └── candidate_profile.html

├── uploads/

│ └── resumes/

├── app.py

├── config.py

├── database.sql

├── requirements.txt

└── README.md

---

## Installation Steps

### 1. Clone the Repository

git clone https://github.com/yourusername/ats-project.git

cd ats-project

### 2. Create a Virtual Environment

python -m venv venv

### 3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### 4. Install Required Packages

pip install -r requirements.txt

### 5. Create MySQL Database

CREATE DATABASE ats_db;

Import the database.sql file into MySQL.

### 6. Configure Database

Update your database credentials in app.py or config.py:

MYSQL_HOST = 'localhost'

MYSQL_USER = 'root'

MYSQL_PASSWORD = 'your_password'

MYSQL_DB = 'ats_db'

### 7. Run the Application

python app.py

---

## Database Fields

### Candidates Table

- Candidate ID
- Full Name
- Email
- Phone Number
- Resume File
- Skills
- Experience
- Qualification
- Application Status
- Applied Date

---

## Future Enhancements

- AI-Based Resume Screening
- Candidate Ranking System
- Interview Scheduling
- Email Notifications
- Recruiter Authentication
- Analytics Dashboard
- Resume Parsing with NLP
- Job Posting Management

---

## Author

Developed by: Barnali Bhowmik

---

## License

This project is created for educational and learning purposes. Feel free to modify and improve it as needed.

⭐ If you find this project useful, please give it a star.
