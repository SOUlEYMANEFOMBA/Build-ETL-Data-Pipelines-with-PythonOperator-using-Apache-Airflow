# Utiliser une image de base avec Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
# COPY main.py ./
# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut
# CMD ["python", "main.py"]
