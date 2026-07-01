from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI(title="Shopyar API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {
        "project": "Shopyar",
        "status": "Running",
        "version": "0.2"
    }

@app.post("/upload")
async def upload_receipt(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "Receipt uploaded successfully",
        "filename": file.filename
    }