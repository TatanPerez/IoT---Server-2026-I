import time
import paho.mqtt.client as mqtt
import json
import random  # Para generar valores aleatorios

mqtt_host = "thingsboard"  # desde contenedor: "thingsboard"; desde WSL: "localhost"
mqtt_port = 1883           # dentro de Docker; desde WSL usa puerto expuesto (ej. 1884)
access_token = "MztEVRLecxb6ENFd0xaQ"

client = mqtt.Client()
client.username_pw_set(access_token)
client.connect(mqtt_host, mqtt_port, 60)

while True:
    # Generar valores aleatorios dentro de un rango
    temperature = round(random.uniform(20.0, 30.0), 1)  # entre 20 y 30 °C
    humidity = round(random.uniform(50, 70), 1)         # entre 50 y 70 %
    
    payload = json.dumps({"temperature": temperature, "humidity": humidity})
    client.publish("v1/devices/me/telemetry", payload)
    print("Mensaje enviado:", payload)
    time.sleep(5)