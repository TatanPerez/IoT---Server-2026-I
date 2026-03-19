# Usa la imagen base de Python 3.11
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia tu script dentro de la imagen
COPY simulator.py .

# Instala librerías necesarias
RUN pip install --no-cache-dir paho-mqtt

# Comando por defecto al iniciar el contenedor
CMD ["python", "simulator.py"]