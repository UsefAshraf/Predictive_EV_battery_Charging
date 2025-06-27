import paho.mqtt.client as mqtt
import ssl
import certifi
import socket

def publish_to_mqtt(soc, soh):
    broker = "4e8d18504a6a43b399cef98d05854c71.s1.eu.hivemq.cloud"
    port = 8883
    username = "Usef_Ashraf_2"
    password = "1234567Aa"

    try:
        client = mqtt.Client(protocol=mqtt.MQTTv5)
        client.username_pw_set(username, password)
        client.tls_set(certifi.where(), tls_version=ssl.PROTOCOL_TLS_CLIENT)

        def on_connect(client, userdata, flags, reasonCode, properties=None):
            if reasonCode == 0:
                print("✅ Connected to HiveMQ Cloud")
            else:
                print(f"❌ Failed to connect, reason code {reasonCode}")

        client.on_connect = on_connect

        print("🔌 Connecting to MQTT broker...")
        client.connect(broker, port)
        client.loop_start()

        client.publish("raspberrypi/soc", f"{round(soc, 2)}")
        client.publish("raspberrypi/soh", f"{round(soh, 2)}")

        print(f"📡 Sent SOC to raspberrypi/soc: {round(soc, 2)}")
        print(f"📡 Sent SOH to raspberrypi/soh: {round(soh, 2)}")

        client.loop_stop()
        client.disconnect()
    except socket.gaierror:
        print("❌ MQTT Error: DNS resolution failed. Check your internet connection.")
    except Exception as e:
        print(f"❌ MQTT Error: {e}")
