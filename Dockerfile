# Utilisation de l'image officielle Python comme base
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de dépendances en premier (optimise le cache Docker)
COPY requirements.txt /app/

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application
COPY app.py /app/

# Exposition du port 5000
EXPOSE 5000

# Définition de la commande de lancement
CMD ["python", "app.py"]
