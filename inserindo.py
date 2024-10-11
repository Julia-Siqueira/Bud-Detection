import cv2
import time
from ultralytics import YOLO
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('yolo_performance.db')
c = conn.cursor()

# Load the YOLO model
path = 'C:\\Users\\ct67ca\\Desktop\\Cana\\runs\\detect\\train2\\weights\\best.pt'
model = YOLO(path)

# Open the video file
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Medir o tempo de preprocessamento
        start_time = time.time()

        # Run YOLO tracking on the frame
        results = model.track(frame, persist=True, conf=0.3)

        # Medir o tempo de inferência
        inference_time = time.time() - start_time

        # Aqui consideramos que o tempo de preprocessamento é o mesmo que o tempo de captura de frame
        preprocess_time = inference_time  # Ajuste conforme necessário
        postprocess_time = 0  # Estime ou calcule conforme necessário

        width, height = frame.shape[1], frame.shape[0]
        detections = len(results[0].boxes)  # Número de caixas detectadas

        # Inserir dados no banco de dados
        c.execute('''
            INSERT INTO performance (preprocess_time, inference_time, postprocess_time, width, height, detections)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (preprocess_time, inference_time, postprocess_time, width, height, detections))

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Commit changes and close connection
conn.commit()
conn.close()

# Release video capture object and close display window
cap.release()
cv2.destroyAllWindows()
