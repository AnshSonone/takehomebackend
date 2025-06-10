from typing import List
from fastapi import FastAPI, HTTPException
from model import  UserModel, response_model, LoginRequest, LoginResponse
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

courses = [
    {"id": 1, "title": "Python", "video_url": "https://youtu.be/fWjsdhR3z3c", "description": "Python ZERo to Hero", "isEnrolled": False},
    {"id": 2, "title": "Java", "video_url": "https://youtu.be/fWjsdhR3z3c", "description": "Java", "isEnrolled": True},
    {"id": 3, "title": "Python Basics", "description": "Learn Python", "video_url": "https://www.youtube.com/", "isEnrolled": False},
    {"id": 4, "title": "Advanced JS", "description": "Deep dive into JavaScript", "video_url": "https://www.youtube.com/", "isEnrolled": True},
    ]

user = {"id": 1, "username": "Jeff", "email": "joff@example.com", "enrolledCourses": [1]}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = []


@app.post("/register", response_model=response_model)
def register_user(user: UserModel):
    # Check for existing username or email
    if any(u["username"] == user.username for u in fake_users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    if any(u["email"] == user.email for u in fake_users_db):
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_password = pwd_context.hash(user.password)

    # Store user
    fake_users_db.append({
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
    })

    return {
        "username": user.username,
        "email": user.email,
        "message": "User registered successfully"
    }

@app.post("/api/login", response_model=LoginResponse)
def login_user(credentials: LoginRequest):

    user = next((u for u in fake_users_db if u["email"] == credentials.email), None)
    
    if user and pwd_context.verify(credentials.password, user["hashed_password"]):
        return {
            "username": user["username"],
            "email": user["email"],
            "message": "Login successful"
        }
    
    raise HTTPException(status_code=401, detail="Invalid email or password")

@app.get("/")
def read_root():
    return {"user": user}

@app.get("/api/courses")
def read_courses():
    return {"courses": courses}

@app.get("/api/courses/{course_id}")
def read_enrolled_course(course_id: int):
    course = next((c for c in courses if c["id"] == course_id), None)
    if course:
        return {"course": course}
    raise HTTPException(status_code=404, detail="Course not found")


@app.get("/api/user")
def read_user():
    return {"user": user}
