# Usa una imagen base que tenga Python y otras dependencias necesarias
FROM python:3.8

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto utilizado por tu aplicación (si es necesario)
EXPOSE 80

# Define el comando para ejecutar tus pruebas
CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results", "features/"]
