from moviepy import ImageClip, AudioFileClip, vfx, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from pathlib import Path

# 🎯 Configuración
IMAGE_PATH = Path("./Images/flesh_torn_from_metal_heart.png")
AUDIO_PATH = Path("./audio/hype_1.mp3")
OUTPUT_PATH = Path("./videos/flesh_torn_from_metal_heart.mp4")
DURATION = 10  # segundos
FPS = 30
WIDTH = 1024  # resolución horizontal

# Crear carpeta de salida
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Cargar la imagen de fondo
imagen_fondo = ImageClip(IMAGE_PATH).with_duration(DURATION)

# Crear el clip de texto
texto = TextClip(text='¡Hola, Mundo!', font_size=70, color='white')

# Poner el texto en el centro
texto = texto.with_position(("center", "bottom")).with_duration(DURATION)

# Componer el texto sobre la imagen de fondo
video = CompositeVideoClip([imagen_fondo, texto])

# Combinar imagen y audio
video_final = video.with_audio(AudioFileClip(AUDIO_PATH).with_duration(DURATION))

# Exportar el video final
video_final.write_videofile(str(OUTPUT_PATH), fps=FPS)
