import paho.mqtt.client as mqtt
import ssl
import time
import random

# MQTT-broker information
broker_address = "localhost"  # Ansluter till Mosquitto som körs lokalt
port = 1883  # Standardport utan TLS

# MQTT-klient-ID och ämne
client_id = "SimulatedSensor"
topic = "sensor/temperature"

# Callback för anslutning
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

# Callback för publicering
def on_publish(client, userdata, mid):
    print("Data published to topic:", topic)

# Skapa MQTT-klient
client = mqtt.Client(client_id)
client.username_pw_set("valskog98", "kaffekopp98")  # Användarnamn och lösenord för brokern
client.on_connect = on_connect
client.on_publish = on_publish

# Anslut till MQTT Broker
client.connect(broker_address, port)
client.loop_start()

try:
    while True:
        # Generera ett slumpmässigt temperaturvärde
        temperature = round(random.uniform(20.0, 30.0), 2)
        print(f"Publishing temperature: {temperature}°C to topic {topic}")
        
        # Publicera temperaturen till MQTT-ämnet
        client.publish(topic, temperature)
        time.sleep(5)  # Publicera varje 5 sekunder

except KeyboardInterrupt:
    print("Simulation stopped.")
finally:
    client.loop_stop()
    client.disconnect()
