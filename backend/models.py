from pydantic import BaseModel

class ChatMessage(BaseModel):
    user: str
    message: str
    timestamp: str

class Symptom(BaseModel):
    name: str
    severity: int

class Hospital(BaseModel):
    name: str
    location: str
    contact: str

class DoctorRecommendation(BaseModel):
    doctor_name: str
    specialization: str
    contact: str