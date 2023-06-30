import paho.mqtt.client as paho
import time
from IPython.display import Audio

broker="157.230.214.127"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass


def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    print(message_received)
    if(message_received=="Sonido"):
       sound_file = 'hum_h.mp3'
       display(Audio(sound_file, autoplay=True))

client1=paho.Client("Python")
client1.on_publish = on_publish    
client1.subscribe("Sensores")
client1.on_message = on_message
client1.connect(broker,port)


while True:                          
                                                               
    #client1.publish("seleccion","plastico")                   
    time.sleep(0.5)
    client1.loop_start()
    client1.subscribe('Sensores')
    #time.sleep(2)
    #client1.loop_stop();
  
