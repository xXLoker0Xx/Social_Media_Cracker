import pandas as pd
import re
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

EXCEL_PATH = "resultados_generados.xlsx"

# ⚙️ Modelo de Ollama
llm = OllamaLLM(model="llama3:instruct")

# 🧠 Prompt para generar títulos distópicos
template = PromptTemplate(
    input_variables=["concepto"],
    template="""
Eres un profesional del marketin. Te dedicas a crear títulos impactantes y emocionales para vídeos distópicos cortos en redes sociales.

Dado el siguiente concepto o escena, genera un título breve de 5 palabras, sin comillas ni signos de puntuación, directo, evocador y visualmente potente.

🎯 Concepto: {concepto}

Título:
"""
)

# 🔗 Cadena de generación
chain = template | llm

# 📥 Cargar títulos existentes del Excel
try:
    df_existente = pd.read_excel(EXCEL_PATH)
    titulos_existentes = set(df_existente["titulo"].str.strip().str.lower())
    # print("los titulos existentes son:")
    # print(titulos_existentes)
except (FileNotFoundError, KeyError):
    titulos_existentes = set()
    df_existente = pd.DataFrame(columns=["titulo", "archivo"])

# ✅ Función para generar un título único y su nombre de imagen
def generar_titulo(concepto: str, intentos=10):
    for _ in range(intentos):
        resultado = chain.invoke({"concepto": concepto}).strip()
        resultado_normalizado = resultado.lower()
        if resultado_normalizado not in titulos_existentes:
            nombre_archivo = re.sub(r'\W+', '_', resultado_normalizado) + ".png"
            return resultado, nombre_archivo
    raise ValueError("❌ No se pudo generar un título único tras varios intentos.")
