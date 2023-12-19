from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from utils import check_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Checker(BaseModel):
    text: str


@app.post("/check")
async def check_text_description(checker: Checker):
    description = check_text(f"Text: {checker.text}")
    return {"Text": description}


