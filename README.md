Backend (FastAPI)

🔗 Hosted URL
https://takehomebackend.onrender.com

Main Features:
Register a new user

Login with email and password

Get a list of courses

Get user info

Get a specific course by ID

CORS Configuration
To allow the frontend (on Vercel) to talk to the backend (on Render), we use CORS middleware like this:

origins = [
    "http://localhost",
    "http://localhost:4200",
    "https://takehomefrontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

This avoids CORS errors by allowing requests only from the deployed frontend.

API Endpoints
Method	Endpoint	Description
POST	/register	Register a new user
POST	/api/login	Login and return user info
GET	/api/courses	Get all available courses
GET	/api/courses/{id}	Get a specific course by ID
GET	/api/user	Get a hardcoded user’s data
GET	/	Base route, returns user info

.

How to Run Locally
Backend
1. open terminal on your machine
2. create directory on your machine name backend or any other name you like
  command: mkdir backend
3. to go into backend directory
  command: cd backend
4. go to github on green color code icon click it and copy https link of github project
5. type git clone command to copy this code in your machine
  command: git clone <paste that_copied_link>
6. inside backend directory you will see takehomebackend directory go inside that directory
  command: cd takehomebackend
7. create virtual environment on takehomebackend directory
   comand: python -m venv .venv
8. this command will create virtual environment on your machine
9. activate your virtual environment
10. for windows this command
    command: .venv/Scripts/activate
11. for linux this command
    command: source .venv/bin/activate
12. you will see before your directory name (.venv) is apprearing like this (.venv) your_username/your_directory/backend/takehomebackend
13. now run this command to install all required dependencies for this project
    command: pip install -r requirements.txt
14. this wiil take time to install all dependencies
15. now you can run your project using
    fastapi dev main.py

How to push code to github

1. Create a New Repository
Click the “+” icon in the top right → New repository

Name it something like:
takehome-fullstack

Add a description (optional)

Choose Public or Private

Don’t initialize with README, .gitignore, or license

Click Create repository

2. Initialize Git Locally
Open your terminal in your project folder and run:
command: git init

3. Create .gitignore
Make sure you don’t commit your virtual environment or build files.

Create a .gitignore file in your root folder and add this thing on .gitignore:

# Python
__pycache__/
*.pyc
.venv/

# Node/Angular
node_modules/
dist/

# OS
.DS_Store

4. Stage and Commit Your Code

command: git add .
git commit -m "Initial commit - FastAPI + Angular project"
5. Push to GitHub

command: git branch -M main
command: git remote add origin https://github.com/YOUR_USERNAME/takehome-fullstack.git
command: git push -u origin main






