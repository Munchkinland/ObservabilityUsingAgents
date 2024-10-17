# Utilizar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y el archivo de configuración de New Relic
COPY requirements.txt ./
COPY newrelic.ini ./

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de tu aplicación
COPY . .

# Configurar la variable de entorno para New Relic
ENV NEW_RELIC_CONFIG_FILE=/app/newrelic.ini

# Comando para ejecutar tu aplicación
CMD ["newrelic-admin", "run-program", "python", "app.py"]
