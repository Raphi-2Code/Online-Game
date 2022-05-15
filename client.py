from ursinanetworking import *
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import threading
import time
from shared import *
#import second_client
app = Ursina()
window.borderless = False

Client = UrsinaNetworkingClient("localhost", 25565)
Blabla = ReplicatedClEventsHandler(Client)

PointLight(position = (4, 1, 4))

def update():
    #Entity(model="cube",position=second_client.player.position)
    Client.process_net_events()
    Blabla.replicated_update()
player = FirstPersonController()
player.gravity=0
player.speed=0
player.collider=None
player.x=3
player.y=6
player.z=3
player.rotation_y=17.22222222222
app.run()