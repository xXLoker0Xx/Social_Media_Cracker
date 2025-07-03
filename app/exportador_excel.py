import os
import pandas as pd
from datetime import datetime

EXCEL_PATH = "resultados_generados.xlsx"

def guardar_resultado(concepto: str, titulo: str, prompt: str, imagen: str = ""):
    data = {
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "concepto": [concepto],
        "titulo": [titulo],
        "prompt": [prompt],
        "imagen": [imagen]
    }

    df_nuevo = pd.DataFrame(data)

    if os.path.exists(EXCEL_PATH):
        df_existente = pd.read_excel(EXCEL_PATH)
        df_total = pd.concat([df_existente, df_nuevo], ignore_index=True)
    else:
        df_total = df_nuevo

    df_total.to_excel(EXCEL_PATH, index=False)
    print(f"📊 Resultado guardado en {EXCEL_PATH}")
