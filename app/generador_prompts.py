from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# ⚙️ Cargar el modelo llama3:instruct desde Ollama
llm = OllamaLLM(model="llama3:instruct")

new_template = PromptTemplate(
    input_variables=["tema", "personaje", "background"],
    template="""
You are a visual prompt generator for cinematic dystopian imagery. Your goal is to generate **one prompt only**, with no explanation.

The image will be vertical (768x1360), designed for a short video. Use the **jibMixRealisticXL** model for hyperrealistic, magical-technological fusion.

Structure:

---

**FOCUS:**  
A person overwhelmed, corrupted, or driven insane by technology. Use symbolic visual elements to show this: wires growing into skin, screens replacing eyes, data spiraling around their head, or magical circuits glowing through the skin.

**MAIN SUBJECT:**  
Describe the person in distress. Indicate age, gender (optional), clothing, visible signs of madness or transformation, posture (e.g., clutching head, screaming silently), and any fusion of organic and synthetic elements. Add glowing tattoos, levitating limbs, broken gadgets, or magical-tech.

**ENVIRONMENT (BACKGROUND):**  
Describe a collapsing or corrupted environment: a digital wasteland, broken VR domes, abandoned labs, shattered neon temples, or overgrown control rooms. Use visual contrasts: organic vs. synthetic, light vs. shadows.

**ATMOSPHERE & MOTION:**  
Include effects like sparks, glitching air, electric mist, magical energy pulses, floating debris, particles or distortions. Simulate mental dissonance and digital overload.

**STYLE & CAMERA:**  
"ultra-detailed, 8K RAW photo, DSLR, cinematic lens flare, hyperreal skin texture, dramatic contrast, volumetric lighting, depth-rich wide-angle shot, magical particles, digital distortion, surreal composition"

---

🎯 Theme: {tema}  
**Protagonist:** {personaje}  
**Background:** {background}

Return only the image prompt. No titles, no extra text. Separate sections by commas.
"""
)

template_completo = PromptTemplate(
    input_variables=["tema", "personaje", "background"],
    template="""
You are a world-class AI prompt engineer. Generate a single visual prompt only, without explanation.

🎯 Objective: Generate a stunning, cinematic, dystopian image, based on the environment.

Use this structure:

---

**ENVIRONMENT / BACKGROUND:** 
Start this part like this:
"The setting around the subject is {background}. " 
Describe with detail the setting around the subject. Use dystopian urban or natural decay elements (ruins, neon lights, abandoned tech, polluted skies, overgrown buildings...). Separate it clearly from the main subject.

**PROTAGONIST:**
Start this part like this:
"The subject is {personaje}. "
Describe a human or creature that fits the dystopian theme. Give details like age, clothing, posture, emotion, accessories, etc. It must be photorealistic and emotionally intense. Focus on facial expression, pose, and mood.

**STYLE & CAMERA:**  
Use literally:  
"ultra-detailed, 8K RAW photo, DSLR, deep focus, wide-angle lens, cinematic framing, volumetric lighting, dramatic shadows, depth-rich, distant perspective, subject small in frame, environment-dominant composition"

---

🎯 Theme: {tema}
**PROTAGONIST:** {personaje},
**ENVIRONMENT / BACKGROUND:** {background}

⚠️ Follow this rules for the output:
1. Output only the prompt.
2. No explanations, no headings.
3. Write it as one continuous prompt, separating subject, background, and style with the titles.
4. Write it in english.

"""
)

prompt_template = PromptTemplate(
    input_variables=["tema", "personaje", "background"],
    template="""
You are a visual prompt generator for impact social media images. Your goal is to generate **one prompt only**, with no explanation.

The prompt should tell a story mixing all the components.

---

**THEME:** {tema}

**MAIN SUBJECT (Protagonist):**  
{personaje}  
Describe the character, sholuld be lost because of technology. Emphasize intense emotional state, natural posture, and surrounding effects.

**BACKGROUND (Environment):**  
{background}  
Describe a decaying setting.

**ATMOSPHERE & MOTION:**  
Add cinematic dynamic elements like sparks flying, glitching shadows, magical particles, smoke and electric mist.

**STYLE & CAMERA:**
The prompt should end:  
ultra-detailed, 8K RAW photo, DSLR, bird's-eye perspective, cinematic lens flare, hyperreal skin texture, dramatic contrast, volumetric lighting, depth-rich wide-angle shot, magical particles, digital distortion, surreal composition

---
⚠️ Follow this rules for the output:
1. Output only the prompt.
2. Do not include titles, headers, or explanations.
3. Must be a single prompt, with the concepts separated by commas.
4. Write it in english.

Example format:
[subject description], [background description], [atmosphere/motion], [style and camera]

Now generate the prompt:

"""
)

# Genera un prompt distópico visual a partir de un tema específico.
def generar_prompt_completo(tema: str, personaje: str = "un humano", background: str = "una ciudad futurista") -> str:
    """
    Genera un prompt distópico visual a partir de un tema, personaje y fondo específicos.
    """
    # ⛓️ Encadenar plantilla y modelo
    chain = prompt_template | llm

    # Personalizar el tema con el personaje y el fondo
    return chain.invoke({"tema": tema, "personaje": personaje, "background": background})
