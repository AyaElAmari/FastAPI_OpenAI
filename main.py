from typing import Union
from fastapi import FastAPI, Response, UploadFile, File
from pydantic import BaseModel
from utils import check_text
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2
import io

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

@app.post("/uploadpdf")
async def upload_pdf(file: UploadFile):
    if file.filename.endswith(".pdf"):
        try:
            # Read the uploaded PDF file
            pdf_contents = await file.read()

            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_contents))

            # Initialize a variable to store the extracted text
            extracted_text = ""

            # Loop through each page and extract text
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                page_text = page.extract_text()
                extracted_text += page_text

            return {"text": extracted_text}

        except Exception as e:
            print("error")
            return {"error": str(e)}
    else:
        print("error")
        return {"error": "Invalid file format. Please upload a PDF file."}
