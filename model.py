from pydantic import BaseModel, EmailStr, constr


class UserModel(BaseModel):
    username: constr(min_length=3)
    email: EmailStr
    password: constr(min_length=8)
    enrolled_courses: list[int] = []

# class CourseModel(BaseModel):
#     id: int
#     title: str
#     video_url: str
#     description: str
#     is_enrolled: bool = False
    
class response_model(BaseModel):
    username: str
    email: EmailStr
    message: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    username: str
    email: EmailStr
    message: str