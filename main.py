# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas>=1.0.0",
#   "numpy>=1.0.0",
#   "sentence-transformers>=2.0.0",
#   "scikit-learn>=0.24.0",
#   "fastapi>=0.68.0",
#   "openpyxl>=3.0.0",
#   "uvicorn>=0.14.0",
#   "python-multipart>=0.0.5",
#   "httpx>=0.3.0",
#   "dotenv>=0.0.1",
# ]
# ///




from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
from llm import ai
from file_handle import upload

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/")
async def questions(
    question: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    try:
        # Save file temporarily if provided
        temp_file_path = None
        if file:
            temp_file_path = await upload(file)
        
        # Get answer from OpenAI
        answer = await ai(question, temp_file_path)
        
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)