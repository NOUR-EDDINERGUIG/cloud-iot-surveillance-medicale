# Cloud IoT – Surveillance médicale multi-patients

Plateforme de surveillance en temps réel de **5 patients** : simulation de signes vitaux, détection d'anomalies et génération d'alertes selon **3 niveaux de criticité**.

## Architecture

```
simulateur_patients.py ──MQTT──▶ Mosquitto ──▶ Node-RED ──▶ InfluxDB ──▶ Grafana
   (signes vitaux)            (broker)   (traitement + alertes) (stockage)  (dashboard)
```

| Service    | Rôle                           | Port  |
|------------|--------------------------------|-------|
| Mosquitto  | Broker MQTT                    | 1883  |
| Node-RED   | Traitement des données, alertes| 1880  |
| InfluxDB   | Base de séries temporelles     | 8086  |
| Grafana    | Visualisation                  | 3000  |

Le simulateur publie sur `patients/<ID>/vitaux` (fréquence cardiaque, température, SpO₂, tension) toutes les 5 secondes, avec ~15 % de valeurs anormales.

## Lancement

```bash
# 1. Démarrer l'infrastructure
docker compose up -d

# 2. Importer le flow : Node-RED (http://localhost:1880) → Menu → Import → nodered/flows.json

# 3. Lancer le simulateur
pip install -r requirements.txt
python simulateur_patients.py
```

Grafana : http://localhost:3000 (source de données InfluxDB : `http://influxdb:8086`, org `medical`, bucket `patients`).

> ⚠️ Les identifiants dans `docker-compose.yml` (`admin123`, `montoken123`) sont des valeurs de **démonstration locale** uniquement. Ne les réutilisez pas en production.

## Technologies
Python · MQTT · Mosquitto · Node-RED · InfluxDB · Grafana · Docker Compose

## Documentation
Rapport complet : [`docs/rapport.pdf`](docs/rapport.pdf)

## Auteur
Nour-eddine Rguig – Master IA & Data Science, Université Mohammed Premier Oujda
