import machine
import secrets
import network
import time
import ussl
from umqtt.simple import MQTTClient

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
led = machine.Pin("LED", machine.Pin.OUT)
led.off()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
max_wait = 10
while max_wait > 0:
 if wlan.status() < 0 or wlan.status() >= 3:
  break
print(wlan.ifconfig())

with open("client2.key", 'rb') as f:
    key = f.read()
with open("client2.crt", 'rb') as f:
    cert = f.read()
ssl_params = dict()
ssl_params["cert"] = cert
ssl_params["key"] = key
ssl_params["cert_reqs"] = ussl.CERT_OPTIONAL
CLIENTID_DEVICEID = "<DEVICE ID>"
MQTTSERVER = "<URL do EVENT GRID NAMESPACES>"
USERNAME = "<DEVICE ID>"
PASSWORD = ""
ssl_params["server_hostname"] = MQTTSERVER
c = MQTTClient(CLIENTID_DEVICEID,MQTTSERVER,user=USERNAME,password=PASSWORD,ssl=True,ssl_params=ssl_params)

c.connect()
led.on()

while True:
    led.on()
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    # devices/temperature = Tópico no MQTT Broker
    c.publish(b"devices/temperature", f"{{\"temperature\": {temperature} }}".encode())
    print(temperature)
    led.off()
    time.sleep(2)
    
c.disconnect()

