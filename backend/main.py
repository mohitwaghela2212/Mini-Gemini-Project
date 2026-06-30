from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()#load environment variables from .env file in the current directory

app = FastAPI()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

app.add_middleware(    #CORS cross origin resource sharing
    CORSMiddleware,
    allow_origins=["*"],              # Allows specific origins
    allow_credentials=True,           # Allows cookies and credentials
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)

class PromptRequest(BaseModel):
    prompt: str
    
@app.post("/generate")
def generate_response(request: PromptRequest):
    response = model.generate_content(request.prompt)
    return {
        "response": response.text
    }
