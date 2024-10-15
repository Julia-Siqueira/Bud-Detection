from fastapi import FastAPI, HTTPException, status, responses, Depends, UploadFile, File, Form
from pydantic import BaseModel, Field
from uuid import UUID
import model
from typing import Optional
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI()

UPLOAD_DIR = "uploads"

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

model.Base.metadata.create_all(bind=engine)

def get_db(): # abrir o banco de dados
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Imagens_cana(BaseModel):
    id: Optional[int] = None
    label: Optional[str] = None
    local_imagem: Optional[str] = None

@app.post("/upload/")
async def upload_imagem(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    
    print(file)
    file_location = f"{UPLOAD_DIR}/{file.filename}"

    # try:
    #     processed_image_location = 

    # with open(file_location, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    
    # modelo_imagens_cana = model.Img_cana()
    # modelo_imagens_cana.local_imagem = file_location
    # modelo_imagens_cana.label = file.filename

    # db.add(modelo_imagens_cana)
    # db.commit()

    # return {"filename": file.filename, "path": file_location, "model": modelo_imagens_cana}

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)