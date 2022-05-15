from ursina import *
from ursinanetworking import *

class TestObject(Button, Replicator):
    def __init__(self, position=(-1,1,0)):

        Button.__init__(
            self,
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'ursxample_stone_tex.bmp',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )

        self.sfx = Audio("ursxample_stone_dig.ogg", autoplay=False)
        Replicator.__init__(self)
        #self.replicate("position")

    def destroy_server(self):
        replicated_destroy(self)
        self.rpc_multicast(self.sfx_multicast, 0.5)

    def place_server(self, pos):
        a = self.replicated_handler.create_replicated_object(TestObject, position = pos)
        self.rpc_multicast(self.sfx_multicast, 1)

    def sfx_multicast(self, pitch):
        self.sfx.pitch = pitch
        self.sfx.play()

    def input(self, key):
        if self.hovered and key == "left mouse down":
            self.rpc_server(self.destroy_server)
        if self.hovered and key == "right mouse down":
            self.rpc_server(self.place_server, self.position + mouse.normal)
class TortObject(Button, Replicator):
    def __init__(self, position=(-1,1,0)):

        Button.__init__(
            self,
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'guy.png',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            rotation_z=90,
            rotation_y=90,
            rotation_x=-90
        )

    need_destroy = False
    replicates = []

    def update(self):
        need_destroy = False
        replicates = []
        if self.intersects().hit:
            print("Ed wins!" if self.z==-2 else "Edz wins!")
            sys.exit()
class TortTObject(Button, Replicator):
    def __init__(self, position=(-1,1,0)):

        Button.__init__(
            self,
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'ursxample_stone_tex.bmp',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            rotation_z=90,
            rotation_y=90,
            rotation_x=-90
        )
    need_destroy=False
    replicates=[]
    def update(self):
        need_destroy=False
        replicates=[]
class GameEndsEdz(Button, Replicator):
    def __init__(self, position=(-1,1,0)):

        Button.__init__(
            self,
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'winner_edz.png',
            color = color.pink,
            rotation_z=90,
            rotation_y=90,
            rotation_x=-90,
            scale=6
        )
    need_destroy=False
    replicates=[]
    def update(self):
        need_destroy=False
        replicates=[]
class GameEndsEd(Button, Replicator):
    def __init__(self, position=(-1,1,0)):

        Button.__init__(
            self,
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'winner_ed.png',
            color = color.pink,
            rotation_z=90,
            rotation_y=90,
            rotation_x=-90,
            scale=6
        )
    need_destroy=False
    replicates=[]
    def update(self):
        need_destroy=False
        replicates=[]
class Box(Button, Replicator):
    def __init__(self, position=(-1,1,0),**kwargs):
        Button.__init__(
            self,
            parent = scene,
            position = position,
            model = 'sphere',
            origin_y = .5,
            texture = 'wine_cask.png',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            rotation_z=90,
            rotation_y=90,
            rotation_x=-90
        )
    need_destroy=False
    replicates=[]

    def update(self):
        need_destroy=False
        replicates=[]
    def input(self, key):
        if key=="w hold":
            self.x-=0.1
        if key=="s hold":
            self.x+=0.1
        if key=="a hold":
            self.z-=0.1
        if key=="d hold":
            self.z+=0.1