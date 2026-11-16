import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime
 
BROKER = "localhost"
PORT = 1883
 
PATIENTS = [
    {"id": "P001", "nom": "Ahmed Benali", "age": 45},
    {"id": "P002", "nom": "Fatima Zahra", "age": 62},
    {"id": "P003", "nom": "Mohamed Alami", "age": 38},
    {"id": "P004", "nom": "Khadija Moussaoui", "age": 71},
    {"id": "P005", "nom": "Youssef Idrissi", "age": 55},
   
]
 
client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()
 
def generer_donnees(patient):
    if random.random() < 0.15:
        bpm = round(random.choice([random.uniform(35, 55), random.uniform(115, 160)]), 1)
        temperature = round(random.choice([random.uniform(34.5, 35.9), random.uniform(38.6, 40.5)]), 1)
        spo2 = round(random.uniform(80, 93), 1)
    else:
        bpm = round(random.gauss(75, 10), 1)
        temperature = round(random.gauss(37.0, 0.3), 1)
        spo2 = round(random.gauss(97, 1.5), 1)
 
    return {
        "patient_id": patient["id"],
        "timestamp": datetime.now().isoformat(),
        "heart_rate": bpm,
        "temperature": temperature,
        "spo2": spo2,
        "systolique": random.randint(110, 140),
        "diastolique": random.randint(70, 90)
    }
 
print("🏥 Démarrage simulation (Mode Données Brutes)...")
 
while True:
    for patient in PATIENTS:
        donnees = generer_donnees(patient)
        topic = f"patients/{patient['id']}/vitaux"
 
        # 1. Envoi vers Node-RED
        client.publish(topic, json.dumps(donnees))
 
        # 2. Affichage simultané dans le terminal (pour ton rapport)
        print(f"  | Patient: {donnees['patient_id']} | Heart Rate: {donnees['heart_rate']} | Temp: {donnees['temperature']}| spo2: {donnees['spo2']}")
 
    time.sleep(5)