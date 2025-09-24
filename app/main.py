from dotenv import load_dotenv
import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil

from agents.orchestrator_agent import OrchestratorAgent

# Load Hugging Face API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()
orchestrator = OrchestratorAgent()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "AI Data & Research Intelligence Agent Backend"}

@app.post("/query")
async def query_agent(file: UploadFile, question: str = Form(...)):
    try:
        os.makedirs("uploads", exist_ok=True)

        filename = file.filename or "uploaded_file"
        content_type = file.content_type or ""

        # Fallback: If no content_type, infer from filename extension
        if not content_type:
            if filename.endswith(".csv"):
                content_type = "text/csv"
            elif filename.endswith((".xls", ".xlsx")):
                content_type = "application/vnd.ms-excel"
            elif filename.endswith(".pdf"):
                content_type = "application/pdf"

        # Normalize file extension
        if content_type == "text/csv" and not filename.endswith(".csv"):
            filename += ".csv"
        elif content_type in [
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ] and not filename.endswith((".xls", ".xlsx")):
            filename += ".xlsx"
        elif content_type == "application/pdf" and not filename.endswith(".pdf"):
            filename += ".pdf"

        file_path = os.path.join("uploads", filename)

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"Saved upload: {file_path}, content_type={content_type}")

        # Route to correct agent
        result = orchestrator.route(file_path, question)
        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


