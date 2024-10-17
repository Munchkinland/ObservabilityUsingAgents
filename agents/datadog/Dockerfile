# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y el código de la aplicación
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el archivo de configuración de New Relic
COPY newrelic.ini .

# Instala el agente de Datadog
RUN apt-get update && \
    apt-get install -y curl && \
    curl -o dd-agent-install.sh -L https://raw.githubusercontent.com/DataDog/datadog-agent/master/cmd/agent/install.sh && \
    bash dd-agent-install.sh --api-key dc7c97f267ce64973d5d095b223d99bc

# Configura el agente de Datadog
COPY datadog.yaml /etc/datadog-agent/datadog.yaml

# Agrega el archivo de configuración de procesos
RUN echo "process_config:\n  enabled: \"true\"" >> /etc/datadog-agent/datadog.yaml

# Habilita la recolección de logs
RUN echo "logs_enabled: true" >> /etc/datadog-agent/datadog.yaml

# Exponer el puerto que utilizará el agente de Datadog (ajusta según sea necesario)
EXPOSE 8126

# Inicia el agente de Datadog y la aplicación Python
CMD ["sh", "-c", "service datadog-agent start && python your_app.py"]
