from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.models import Imagem
from app.database import get_db
import cv2
import os
import supervision as sv
from ultralytics import YOLO
from fastapi.templating import Jinja2Templates




router = APIRouter()

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Caminho do analisador
path = 'C:\\Users\\ct67ca\\Desktop\\Cana\\runs\\train4\\weights\\best.pt'
model = YOLO(path)

# templates = Jinja2Templates(directory="app/templates")

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Salvar a imagem
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(image_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Processar a imagem
    frame = cv2.imread(image_path)
    if frame is None:
        return {"error": "Erro ao abrir a imagem"}, 400

    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    image = model(frame)[0]
    detections = sv.Detections.from_ultralytics(image)

    labels = [
        f"{class_name}{confidence:.2f}"
        for class_name, confidence in zip(detections['class_name'], detections.confidence)
    ]

    annotated_frame = box_annotator.annotate(scene=frame, detections=detections)
    annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections, labels=labels)

    result_path = os.path.join(RESULTS_FOLDER, file.filename)
    cv2.imwrite(result_path, annotated_frame)


    # Salvar no banco de dados
    db.add(Imagem(nome=file.filename, caminho=result_path))
    db.commit()

    return({"request": {}, "filename": file.filename})

@router.get("/results/{filename}", response_class=HTMLResponse)

async def get_result(filename: str):
    return RedirectResponse(url=f"/results/{filename}")

 # preciso pegar o numero de unhealthy e healthy através do banco de dados
 # uma coluna para cada
 # retornar dados da camera em banco separado

