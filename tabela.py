import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('yolo_performance.db')

# Criar um cursor
c = conn.cursor()

# Criar tabela
c.execute('''
    CREATE TABLE IF NOT EXISTS performance (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        preprocess_time REAL,
        inference_time REAL,
        postprocess_time REAL,
        width INTEGER,
        height INTEGER,
        detections INTEGER
    )
''')

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
