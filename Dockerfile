# Imagen base oficial de Python
FROM python:3.10-slim

# Crear entorno virtual
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app .

# Comando por defecto
CMD ["python", "main.py"]
