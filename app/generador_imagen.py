import requests
import base64
import os

# URL de tu instancia de Stable Diffusion local
URL_SD = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# Negative prompt base para calidad
negative_prompt = (
    "lowres, bad anatomy, bad hands, missing fingers, extra digits, cropped, "
    "worst quality, low quality, jpeg artifacts, blurry, text, watermark, signature, "
    "cartoon, anime, painting, illustration, mutated hands, nsfw, nude, naked, topless"
)

loras = "lora:SDXLFaeTastic2400:0.7"

model_cyber = "cyberrealistic_v80.safetensors [4a74f783f5]"
model_jib = "jibMixRealisticXL_v170SmokeSheen.safetensors [6afe81df3d]"

def generar_imagen(prompt: str, nombre_archivo: str = "output.png"):
    """
    Envía un prompt a la API de Stable Diffusion y guarda la imagen resultante.
    """
    payload = {
        "prompt": loras + ", " + prompt,
        "negative_prompt": negative_prompt,
        "steps": 25,
        "width": 768,
        "height": 1360,
        "cfg_scale": 7,
        "denoising_strength": 0.4,
        "sampler_index": "DPM++ 2M Karras",
        "override_settings": {
            "sd_model_checkpoint": model_cyber
        }
    }

    # Realiza la solicitud a la API de Stable Diffusion (que es tu servidor local)
    response = requests.post(URL_SD, json=payload)
    print("🛰️ Estado HTTP:", response.status_code)

    # Prepara la ruta de salida
    output_dir = "imagenes_generadas"
    os.makedirs(output_dir, exist_ok=True)  # crea la carpeta si no existe

    try:
        r = response.json()
        if "images" in r:
            image_data = r["images"][0]
            # Nombre del archivo dentro de la nueva carpeta
            ruta_imagen = os.path.join(output_dir, nombre_archivo)

            with open(ruta_imagen, "wb") as f:
                f.write(base64.b64decode(image_data.split(",", 1)[-1]))
            print(f"✅ Imagen guardada como {nombre_archivo}")
            return nombre_archivo
        else:
            print("❌ La API no devolvió imágenes.")
            print("🔍 Respuesta:", r)
            return None
    except Exception as e:
        print("❌ Error procesando respuesta:", e)
        print(response.text)
        return None
