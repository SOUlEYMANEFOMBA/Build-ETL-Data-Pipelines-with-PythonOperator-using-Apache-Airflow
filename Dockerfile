# # Utiliser l'image de base officielle d'Apache Airflow
FROM apache/airflow:2.5.2

# Définir le répertoire de travail
WORKDIR /opt/airflow
##Copie le scipt init_airflow dans le container

COPY init_airflow.sh /opt/airflow/init_airflow.sh
USER root
RUN chmod +x /opt/airflow/init_airflow.sh
# Revir à user airflow

USER airflow

