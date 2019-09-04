from direct.showbase.ShowBase import ShowBase, DirectionalLight, AmbientLight
from panda3d.core import GeoMipTerrain, VBase4
from re import split

from camera import CameraController


def get_vbase4_from_hex(hex_value):
    if hex_value.startswith('#'):
        return get_vbase4_from_hex(hex_value[1:])

    value = [int(x, 16) / 255.0 for x in split('([0-9a-f]{2})', hex_value.lower()) if x != '']
    if len(value) == 3:
        value.append(1)
    return VBase4(value[0], value[1], value[2], value[3])


class MyApp(ShowBase):  # our 'class'

    def __init__(self):
        ShowBase.__init__(self)  # initialise
        self.terrain = GeoMipTerrain("worldTerrain")  # create a terrain
        self.terrain.setHeightfield("heightmapper-1567436259173.png")  # set the height map
        self.terrain.setColorMap("TexturesCom_Moss0138_2_L.jpg")  # set the colour map
        self.terrain.setBruteforce(True)  # level of detail
        root = self.terrain.getRoot()  # capture root
        root.reparentTo(self.render)  # render from root
        root.setSz(80)  # maximum height
        self.terrain.generate()  # generate
        self.sphere = self.loader.loadModel("skysphere-1.egg")

        self.sphere.setScale(700)
        self.sphere.setPos(500, 500, 0)

        self.tex = self.loader.loadTexture("TexturesCom_Skies0282_L.jpg")
        self.sphere.setTexture(self.tex)

        self.sphere.reparentTo(self.render)
        self.setupLight()   

    def setupLight(self):
        self.sunLight = DirectionalLight("sun")
        # sunLight.setColor(get_vbase4_from_hex('fbfcde'))
        self.sunLight.setColor(VBase4(.99, .99, .99, 1))
        self.light = self.render.attach_new_node(self.sunLight)
        self.light.setHpr(45, -45, 0)
        self.light.setPos(0, 0, 300)
        self.render.setLight(self.light)

        ambientLight = AmbientLight("ambient")
        ambientLight.setColor(VBase4(0.2, 0.2, 0.2, 1))
        self.ambientLight = self.render.attach_new_node(ambientLight)
        self.render.setLight(self.ambientLight)
        return


app = MyApp()
app.run()
