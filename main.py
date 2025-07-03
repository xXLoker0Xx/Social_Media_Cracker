# This script generates a dystopian video based on a given theme.
from app.generador_prompts import generar_prompt_completo
from app.generador_imagen import generar_imagen
from app.generador_titulos import generar_titulo

from app.exportador_excel import guardar_resultado


def generar_video_distopico(tema: str, personaje: str = "un humano", background: str = "una ciudad futurista"):
    """
    Genera un video distópico a partir de un tema dado.
    """
    # Generar prompt
    print("📡 Generando prompt...")
    prompt = generar_prompt_completo(tema, personaje, background)
    print(prompt)

    # Generar título
    print("📡 Generando títulos...")
    titulo, titulo_imagen = generar_titulo(tema)
    print(titulo_imagen)
    
    # Generar imagen
    print("📡 Enviando solicitud a Stable Diffusion...")
    generar_imagen(prompt, titulo_imagen)

    # Guardar resultado en Excel
    print(f"📊 Exportando a excel...")
    guardar_resultado(tema, titulo, prompt, titulo_imagen)


if __name__ == "__main__":
    tema = "man lost in social media"
    personaje = "35 year old nerd in the computer"
    background = "a creepy room of a nerd"
    generar_video_distopico(tema, personaje, background)
