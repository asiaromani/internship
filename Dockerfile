# Utilisez une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de votre application dans le conteneur
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exposer le port que votre application Flask utilise
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["flask", "run"]

