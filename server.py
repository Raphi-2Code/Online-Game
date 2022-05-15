from ursinanetworking import *
from shared import *
#import client
#import second_client
Server = UrsinaNetworkingServer("localhost", 25565)
Blabla = ReplicatedSvEventsHandler(Server)
i=0
for z in range(6):
    for x in range(6):
        i=i+1
        new_block = Blabla.create_replicated_object(TestObject, position = (x, 0, z))
ed=Blabla.create_replicated_object(TortObject,position=(3,0.15,-2))
edz=Blabla.create_replicated_object(TortObject,position=(3,0.15,6))
for zt in range(6):
    for xt in range(6):
        ground=Blabla.create_replicated_object(TortTObject,position=(xt,-1,zt-0.5))
box=Blabla.create_replicated_object(Box,position=(0,0.55,0))
#def update():
while True:
    Server.process_net_events()
    Blabla.replicated_update()