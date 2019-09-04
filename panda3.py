from direct.showbase.ShowBase import ShowBase, DirectionalLight, VBase4, TextNode, GeoMipTerrain
from direct.gui.DirectGui import *
from direct.task import Task
from math import pi, sin, cos
from panda3d.core import WindowProperties


UPPER_POS_LIMIT = 5000
LOWER_POS_LIMIT = -5000
COLOR_RANGE = (0, 1)
SIZE_RANGE = (0.1, 3000)

POS_RANGE = (LOWER_POS_LIMIT, UPPER_POS_LIMIT)
ANGLE_RANGE = (-360, 360)

LABEL_FG = (1, 1, 1, 1)
LABEL_BG = (0, 0, 0, 1)

"""
Sky position                :  LPoint3f(500, 500, 0)
Sky scale                   :  LVecBase3f(900, 900, 900)
Sky size                    :  900.0
Terrain position            :  LPoint3f(500, 500, 0)
Camera x                    :  0
Camera y                    :  0
Camera z                    :  0
Camera yaw                  :  0
Camera pitch                :  0
Camera roll                 :  0
Sunlight red                :  0.9200000166893005
Sunlight green              :  0.9100000262260437
Sunlight blue               :  0.9100000262260437
Sunlight yaw                :  0.0
Sunlight pitch              :  0.0
Sunlight roll               :  0.0



Sky position                :  LPoint3f(296.9, 500, 0)
Sky scale                   :  LVecBase3f(592.524, 592.524, 592.524)
Sky size                    :  592.5240478515625
Terrain position            :  LPoint3f(-217.464, 90.0205, 0)
Camera x                    :  204
Camera y                    :  -256
Camera z                    :  153
Camera yaw                  :  0
Camera pitch                :  -14
Camera roll                 :  0
Sunlight red                :  0.9200000166893005
Sunlight green              :  0.9100000262260437
Sunlight blue               :  0.9100000262260437
Sunlight yaw                :  -14.75927734375
Sunlight pitch              :  -33.208526611328125
Sunlight roll               :  0.0

"""

DEFAULT_CAMERA_X = 204
DEFAULT_CAMERA_Y = -256
DEFAULT_CAMERA_Z = 153
DEFAULT_SUN_RED = 0.92
DEFAULT_SUN_GREEN = 0.91
DEFAULT_SUN_BLUE = 0.91
DEFAULT_SUN_ALPHA = 1
DEFAULT_SCENE_SCALE = 0.25
DEFAULT_LIGHT_YAW = -15
DEFAULT_LIGHT_PITCH = -33
DEFAULT_LIGHT_ROLL = 0
DEFAULT_CAMERA_HEADING = 0
DEFAULT_CAMERA_PITCH = -14
DEFAULT_CAMERA_ROll = 0
DEFAULT_SPHERE_X = 297
DEFAULT_SPHERE_Y = 500
DEFAULT_SPHERE_Z = 0
DEFAULT_SPHERE_SZ = 592.524
DEFAULT_SPHERE_SCALE = 592.524
DEFAULT_TERRAIN_X = -217.464
DEFAULT_TERRAIN_Y = 90.0205
DEFAULT_TERRAIN_Z = 0


class MyGUI(object):

    def __init__(self, show_base):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1),
                                 frameSize=(-1, 1, -1, 1),
                                 pos=(1, -1, -1))
        self.slider_camera_x = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_CAMERA_X, pageSize=0.1,
                                            command=self.update_camera_x)
        self.slider_camera_x.setScale(0.2)
        self.slider_camera_x.setPos(-0.5, 0.0, 0.95)

        self.label_camera_x = DirectLabel(parent=self.frame, text='Camera x-axis')
        self.label_camera_x.setScale(0.03)
        self.label_camera_x.setPos(-0.85, 0.0, 0.95)

        self.slider_camera_y = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_CAMERA_Y, pageSize=0.1,
                                            command=self.update_camera_y)
        self.slider_camera_y.setScale(0.2)
        self.slider_camera_y.setPos(-0.5, 0, 0.85)

        self.label_camera_y = DirectLabel(parent=self.frame, text='Camera y-axis')
        self.label_camera_y.setScale(0.03)
        self.label_camera_y.setPos(-0.85, -1, 0.85)

        self.slider_camera_z = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_CAMERA_Z, pageSize=0.1,
                                            command=self.update_camera_z)
        self.slider_camera_z.setScale(0.2)
        self.slider_camera_z.setPos(-0.5, 0, 0.75)

        self.label_camera_z = DirectLabel(parent=self.frame, text='Camera z-axis')
        self.label_camera_z.setScale(0.03)
        self.label_camera_z.setPos(-0.85, 0, 0.75)

        self.slider_camera_heading = DirectSlider(parent=self.frame, range=(-360, 360), value=DEFAULT_CAMERA_HEADING,
                                                  pageSize=0.1,
                                                  command=self.update_camera_heading)
        self.slider_camera_heading.setScale(0.2)
        self.slider_camera_heading.setPos(-0.5, 0, 0.65)

        self.label_camera_heading = DirectLabel(parent=self.frame, text='Camera heading')
        self.label_camera_heading.setScale(0.03)
        self.label_camera_heading.setPos(-0.85, 0, 0.65)

        self.slider_camera_pitch = DirectSlider(parent=self.frame, range=(-360, 360), value=DEFAULT_CAMERA_PITCH,
                                                pageSize=0.1,
                                                command=self.update_camera_pitch)
        self.slider_camera_pitch.setScale(0.2)
        self.slider_camera_pitch.setPos(-0.5, 0, 0.55)

        self.label_camera_pitch = DirectLabel(parent=self.frame, text='Camera pitch')
        self.label_camera_pitch.setScale(0.03)
        self.label_camera_pitch.setPos(-0.85, 0, 0.55)

        self.slider_camera_roll = DirectSlider(parent=self.frame, range=(-360, 360), value=DEFAULT_CAMERA_ROll,
                                               pageSize=0.1,
                                               command=self.update_camera_roll)
        self.slider_camera_roll.setScale(0.2)
        self.slider_camera_roll.setPos(-0.5, 0, 0.45)

        self.label_camera_roll = DirectLabel(parent=self.frame, text='Camera roll')
        self.label_camera_roll.setScale(0.03)
        self.label_camera_roll.setPos(-0.85, 0, 0.45)

        self.slider_sun_red = DirectSlider(parent=self.frame, range=COLOR_RANGE, value=DEFAULT_SUN_RED, pageSize=0.01,
                                           command=self.update_sun_red)
        self.slider_sun_red.setScale(0.2)
        self.slider_sun_red.setPos(-0.5, 0, 0.35)

        self.label_sun_red = DirectLabel(parent=self.frame, text='Light red channel')
        self.label_sun_red.setScale(0.03)
        self.label_sun_red.setPos(-0.85, 0, 0.35)

        self.slider_sun_green = DirectSlider(parent=self.frame, range=COLOR_RANGE, value=DEFAULT_SUN_GREEN,
                                             pageSize=0.01,
                                             command=self.update_sun_green)
        self.slider_sun_green.setScale(0.2)
        self.slider_sun_green.setPos(-0.5, 0, 0.25)

        self.label_sun_green = DirectLabel(parent=self.frame, text='Light green channel')
        self.label_sun_green.setScale(0.03)
        self.label_sun_green.setPos(-0.85, 0, 0.25)

        self.slider_sun_blue = DirectSlider(parent=self.frame, range=COLOR_RANGE, value=DEFAULT_SUN_BLUE, pageSize=0.01,
                                            command=self.update_sun_blue)
        self.slider_sun_blue.setScale(0.2)
        self.slider_sun_blue.setPos(-0.5, 0, 0.15)

        self.label_sun_blue = DirectLabel(parent=self.frame, text='Light blue channel')
        self.label_sun_blue.setScale(0.03)
        self.label_sun_blue.setPos(-0.85, 0, 0.15)

        self.slider_sun_yaw = DirectSlider(parent=self.frame, range=ANGLE_RANGE, value=DEFAULT_LIGHT_YAW, pageSize=0.1,
                                           command=self.update_sun_yaw)
        self.slider_sun_yaw.setScale(0.2)
        self.slider_sun_yaw.setPos(0.2, 0, 0.95)

        self.label_sun_yaw = DirectLabel(parent=self.frame, text='Light yaw')
        self.label_sun_yaw.setScale(0.03)
        self.label_sun_yaw.setPos(-0.15, 0, 0.95)

        self.slider_sun_pitch = DirectSlider(parent=self.frame, range=ANGLE_RANGE, value=DEFAULT_LIGHT_PITCH,
                                             pageSize=0.1,
                                             command=self.update_sun_pitch)
        self.slider_sun_pitch.setScale(0.2)
        self.slider_sun_pitch.setPos(0.2, 0, 0.85)

        self.label_sun_pitch = DirectLabel(parent=self.frame, text='Light pitch')
        self.label_sun_pitch.setScale(0.03)
        self.label_sun_pitch.setPos(-0.15, 0, 0.85)

        self.slider_sun_roll = DirectSlider(parent=self.frame, range=ANGLE_RANGE, value=DEFAULT_LIGHT_ROLL,
                                            pageSize=0.1,
                                            command=self.update_sun_roll)
        self.slider_sun_roll.setScale(0.2)
        self.slider_sun_roll.setPos(0.2, 0, 0.75)

        self.label_sun_roll = DirectLabel(parent=self.frame, text='Light roll')
        self.label_sun_roll.setScale(0.03)
        self.label_sun_roll.setPos(-0.15, 0, 0.75)

        self.slider_sphere_x = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_SPHERE_X, pageSize=0.1,
                                            command=self.update_sphere_x)
        self.slider_sphere_x.setScale(0.2)
        self.slider_sphere_x.setPos(0.2, 0, 0.65)

        self.label_sphere_x = DirectLabel(parent=self.frame, text='Sky x-axis')
        self.label_sphere_x.setScale(0.03)
        self.label_sphere_x.setPos(-0.15, 0, 0.65)

        self.slider_sphere_y = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_SPHERE_Y, pageSize=0.1,
                                            command=self.update_sphere_y)
        self.slider_sphere_y.setScale(0.2)
        self.slider_sphere_y.setPos(0.2, 0, 0.55)

        self.label_sphere_y = DirectLabel(parent=self.frame, text='Sky y-axis')
        self.label_sphere_y.setScale(0.03)
        self.label_sphere_y.setPos(-0.15, 0, 0.55)

        self.slider_sphere_z = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_SPHERE_Z, pageSize=0.1,
                                            command=self.update_sphere_z)
        self.slider_sphere_z.setScale(0.2)
        self.slider_sphere_z.setPos(0.2, 0, 0.45)

        self.label_sphere_z = DirectLabel(parent=self.frame, text='Sky z-axis')
        self.label_sphere_z.setScale(0.03)
        self.label_sphere_z.setPos(-0.15, 0, 0.45)

        self.slider_sphere_sz = DirectSlider(parent=self.frame, range=SIZE_RANGE, value=DEFAULT_SPHERE_SZ, pageSize=0.1,
                                             command=self.update_sphere_sz)
        self.slider_sphere_sz.setScale(0.2)
        self.slider_sphere_sz.setPos(0.2, 0, 0.35)

        self.label_sphere_sz = DirectLabel(parent=self.frame, text='Sky size')
        self.label_sphere_sz.setScale(0.03)
        self.label_sphere_sz.setPos(-0.15, 0, 0.35)

        self.slider_sphere_scale = DirectSlider(parent=self.frame, range=SIZE_RANGE, value=DEFAULT_SPHERE_SCALE,
                                                pageSize=0.1,
                                                command=self.update_sphere_scale)
        self.slider_sphere_scale.setScale(0.2)
        self.slider_sphere_scale.setPos(0.2, 0, 0.25)

        self.label_sphere_scale = DirectLabel(parent=self.frame, text='Sky scale')
        self.label_sphere_scale.setScale(0.03)
        self.label_sphere_scale.setPos(-0.15, 0, 0.25)

        self.button_sphere = DirectButton(parent=self.frame, text="Debug values", command=self.debug_values)
        self.button_sphere.setScale(0.03)
        self.button_sphere.setPos(0.6, 0, 0.95)

        self.slider_terrain_x = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_TERRAIN_X, pageSize=0.1,
                                             command=self.update_terrain_x)
        self.slider_terrain_x.setScale(0.2)
        self.slider_terrain_x.setPos(0.75, 0, 0.85)

        self.label_terrain_x = DirectLabel(parent=self.frame, text='Terrain x-axis')
        self.label_terrain_x.setScale(0.03)
        self.label_terrain_x.setPos(0.55, 0, 0.85)

        self.slider_terrain_y = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_TERRAIN_Y, pageSize=0.1,
                                             command=self.update_terrain_y)
        self.slider_terrain_y.setScale(0.2)
        self.slider_terrain_y.setPos(0.75, 0, 0.75)

        self.label_terrain_y = DirectLabel(parent=self.frame, text='Terrain y-axis')
        self.label_terrain_y.setScale(0.03)
        self.label_terrain_y.setPos(0.55, 0, 0.75)

        self.slider_terrain_z = DirectSlider(parent=self.frame, range=POS_RANGE, value=DEFAULT_TERRAIN_Z, pageSize=0.1,
                                             command=self.update_terrain_z)
        self.slider_terrain_z.setScale(0.2)
        self.slider_terrain_z.setPos(0.75, 0, 0.65)

        self.label_terrain_z = DirectLabel(parent=self.frame, text='Terrain z-axis')
        self.label_terrain_z.setScale(0.03)
        self.label_terrain_z.setPos(0.55, 0, 0.65)

        self.show_base = show_base

    def update_camera_x(self):
        if self.show_base:
            self.show_base.camera_x = int(self.slider_camera_x['value'])

    def update_camera_z(self):
        if self.show_base:
            self.show_base.camera_z = int(self.slider_camera_z['value'])

    def update_camera_y(self):
        if self.show_base:
            self.show_base.camera_y = int(self.slider_camera_y['value'])

    def update_camera_heading(self):
        if self.show_base:
            self.show_base.camera_heading = int(self.slider_camera_heading['value'])

    def update_camera_pitch(self):
        if self.show_base:
            self.show_base.camera_pitch = int(self.slider_camera_pitch['value'])

    def update_camera_roll(self):
        if self.show_base:
            self.show_base.camera_roll = int(self.slider_camera_roll['value'])

    def update_sun_red(self):
        if self.show_base:
            self.show_base.sun_red = float(self.slider_sun_red['value'])

    def update_sun_green(self):
        if self.show_base:
            self.show_base.sun_green = float(self.slider_sun_green['value'])

    def update_sun_blue(self):
        if self.show_base:
            self.show_base.sun_blue = float(self.slider_sun_blue['value'])

    def update_sun_yaw(self):
        if self.show_base:
            self.show_base.sun_yaw = float(self.slider_sun_yaw['value'])

    def update_sun_pitch(self):
        if self.show_base:
            self.show_base.sun_pitch = float(self.slider_sun_pitch['value'])

    def update_sun_roll(self):
        if self.show_base:
            self.show_base.sun_roll = float(self.slider_sun_roll['value'])

    def update_sphere_x(self):
        if self.show_base:
            self.show_base.sphere_x = float(self.slider_sphere_x['value'])

    def update_sphere_y(self):
        if self.show_base:
            self.show_base.sphere_y = float(self.slider_sphere_y['value'])

    def update_sphere_z(self):
        if self.show_base:
            self.show_base.sphere_z = float(self.slider_sphere_z['value'])

    def update_sphere_sz(self):
        if self.show_base:
            self.show_base.sphere_sz = float(self.slider_sphere_sz['value'])

    def update_sphere_scale(self):
        if self.show_base:
            self.show_base.sphere_scale = float(self.slider_sphere_scale['value'])

    def debug_values(self):
        print("Sky position".ljust(28) + ":  " + str(self.show_base.sphere.getPos()))
        print("Sky scale".ljust(28) + ":  " + str(self.show_base.sphere.getScale()))
        print("Sky size".ljust(28) + ":  " + str(self.show_base.sphere.getSz()))
        print("Terrain position".ljust(28) + ":  " + str(self.show_base.root.getPos()))
        print("Camera x".ljust(28) + ":  " + str(self.show_base.camera_x))
        print("Camera y".ljust(28) + ":  " + str(self.show_base.camera_y))
        print("Camera z".ljust(28) + ":  " + str(self.show_base.camera_z))
        print("Camera yaw".ljust(28) + ":  " + str(self.show_base.camera_heading))
        print("Camera pitch".ljust(28) + ":  " + str(self.show_base.camera_pitch))
        print("Camera roll".ljust(28) + ":  " + str(self.show_base.camera_roll))
        print("Sunlight red".ljust(28) + ":  " + str(self.show_base.sun_red))
        print("Sunlight green".ljust(28) + ":  " + str(self.show_base.sun_green))
        print("Sunlight blue".ljust(28) + ":  " + str(self.show_base.sun_blue))
        print("Sunlight yaw".ljust(28) + ":  " + str(self.show_base.sun_yaw))
        print("Sunlight pitch".ljust(28) + ":  " + str(self.show_base.sun_pitch))
        print("Sunlight roll".ljust(28) + ":  " + str(self.show_base.sun_roll))

    def update_terrain_x(self):
        if self.show_base:
            self.show_base.terrain_x = float(self.slider_terrain_x['value'])

    def update_terrain_y(self):
        if self.show_base:
            self.show_base.terrain_y = float(self.slider_terrain_y['value'])

    def update_terrain_z(self):
        if self.show_base:
            self.show_base.terrain_z = float(self.slider_terrain_z['value'])


class MyApp(ShowBase):

    def __init__(self, **kwargs):
        ShowBase.__init__(self)
        self._angle_degrees = 30
        self._angle_radians = self._angle_degrees * (pi / 180.0)
        self._camera_x = DEFAULT_CAMERA_X
        self._camera_y = DEFAULT_CAMERA_Y
        self._camera_z = DEFAULT_CAMERA_Z
        self._sun_red = DEFAULT_SUN_RED
        self._sun_green = DEFAULT_SUN_GREEN
        self._sun_blue = DEFAULT_SUN_BLUE
        self._sun_alpha = 1
        self._scene_scale = 0.25
        self._light_yaw = DEFAULT_LIGHT_YAW
        self._light_pitch = DEFAULT_LIGHT_PITCH
        self._light_roll = DEFAULT_LIGHT_ROLL
        self._camera_heading = DEFAULT_CAMERA_HEADING
        self._camera_pitch = DEFAULT_CAMERA_PITCH
        self._camera_roll = DEFAULT_CAMERA_ROll
        self._sphere_x = DEFAULT_SPHERE_X
        self._sphere_y = DEFAULT_SPHERE_Y
        self._sphere_z = DEFAULT_SPHERE_Z
        self._sphere_sz = DEFAULT_SPHERE_SZ
        self._sphere_scale = DEFAULT_SPHERE_SCALE
        self._terrain_x = DEFAULT_TERRAIN_X
        self._terrain_y = DEFAULT_TERRAIN_Y
        self._terrain_z = DEFAULT_TERRAIN_Z
        if 'gui' in kwargs:
            self.gui = kwargs.get('gui', False)
        else:
            self.gui = False

        self.load_scene()
        if self.gui:
            self.handler = MyGUI(self)

    def load_scene(self):
        self.terrain = GeoMipTerrain("worldTerrain")  # create a terrain
        self.terrain.setHeightfield("goe-height-merged.jpg")  # set the height map
        self.terrain.setColorMap("moss-2.png")  # set the colour map
        # self.terrain.setBruteforce(True)  # level of detail
        self.terrain.setBlockSize(16)
        self.terrain.setAutoFlatten(GeoMipTerrain.AFMStrong)
        self.terrain.setNear(40)
        self.terrain.setFar(100)
        self.root = self.terrain.getRoot()  # capture root
        self.root.reparentTo(self.render)
        self.root.setSz(80)
        self.terrain.generate()

        self.sphere = self.loader.loadModel("skysphere-1.egg")
        self.tex = self.loader.loadTexture("TexturesCom_Skies0282_L.jpg")
        self.sphere.reparentTo(self.render)
        self.sphere.setTexture(self.tex, 1)
        self.sphere.setScale(1207)
        self.sphere.setSz(1207)
        self.sphere.setPos(858, 500, 0)

        self.scene = None
        self.camera.setPos(0, 0, 3)
        self.setupLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                        (self._light_yaw, self._light_pitch, self._light_roll))
        self.render.setShaderAuto()
        if self.gui:
            self.disable()

        self.taskMgr.add(self.updateTerrainTask)

    def disable(self):
        self.disableMouse()

    def enable(self):
        self.enableMouse()

    @property
    def camera_x(self):
        return self._camera_x

    @camera_x.setter
    def camera_x(self, camera_x):
        self._camera_x = camera_x
        self.camera.setPos(self.camera_x, self._camera_y, self._camera_z)

    @property
    def camera_y(self):
        return self._camera_y

    @camera_y.setter
    def camera_y(self, camera_y):
        self._camera_y = camera_y
        self.camera.setPos(self.camera_x, self._camera_y, self._camera_z)

    @property
    def camera_z(self):
        return self._camera_z

    @camera_z.setter
    def camera_z(self, camera_z):
        self._camera_z = camera_z
        self.camera.setPos(self.camera_x, self._camera_y, self._camera_z)

    @property
    def angle_degrees(self):
        return self._angle_degrees

    @angle_degrees.setter
    def angle_degrees(self, anglede_grees):
        self._angle_degrees = anglede_grees
        self._angle_radians = self._angle_degrees * (pi / 180.0)
        self.camera.setPos(20 * sin(self._angle_radians), -20.0 * cos(self._angle_radians), 3)

    @property
    def angle_radians(self):
        return self._angle_radians

    @angle_radians.setter
    def angle_radians(self, angle_radians):
        self._angle_radians = angle_radians
        self._angle_degrees = self._angle_radians / pi * 180
        self.camera.setPos(20 * sin(self._angle_radians), -20.0 * cos(self._angle_radians), 3)

    @property
    def sun_red(self):
        return self._sun_red

    @sun_red.setter
    def sun_red(self, sun_red):
        self._sun_red = sun_red
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def sun_green(self):
        return self._sun_green

    @sun_green.setter
    def sun_green(self, sun_green):
        self._sun_green = sun_green
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def sun_blue(self):
        return self._sun_blue

    @sun_blue.setter
    def sun_blue(self, sun_blue):
        self._sun_blue = sun_blue
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def sun_alpha(self):
        return self._sun_alpha

    @sun_alpha.setter
    def sun_alpha(self, sun_alpha):
        self._sun_alpha = sun_alpha
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def scene_scale(self):
        return self._scene_scale

    @scene_scale.setter
    def scene_scale(self, scene_scale):
        if self.scene is None:
            self._scene_scale = scene_scale
            self.scene.setScale(self._scene_scale, self._scene_scale, self._scene_scale)

    @property
    def sun_yaw(self):
        return self._light_yaw

    @sun_yaw.setter
    def sun_yaw(self, sun_yaw):
        self._light_yaw = sun_yaw
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def sun_pitch(self):
        return self._light_pitch

    @sun_pitch.setter
    def sun_pitch(self, sun_pitch):
        self._light_pitch = sun_pitch
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def sun_roll(self):
        return self._light_roll

    @sun_roll.setter
    def sun_roll(self, sun_roll):
        self._light_roll = sun_roll
        self.updateLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                         (self._light_yaw, self._light_pitch, self._light_roll))

    @property
    def camera_heading(self):
        return self._camera_heading

    @camera_heading.setter
    def camera_heading(self, value):
        self._camera_heading = value
        self.camera.setHpr(self._camera_heading, self._camera_pitch, self._camera_roll)

    @property
    def camera_pitch(self):
        return self._camera_pitch

    @camera_pitch.setter
    def camera_pitch(self, value):
        self._camera_pitch = value
        self.camera.setHpr(self._camera_heading, self._camera_pitch, self._camera_roll)

    @property
    def camera_roll(self):
        return self._camera_roll

    @camera_roll.setter
    def camera_roll(self, value):
        self._camera_roll = value
        self.camera.setHpr(self._camera_heading, self._camera_pitch, self._camera_roll)

    @property
    def sphere_x(self):
        return self._sphere_x

    @sphere_x.setter
    def sphere_x(self, value):
        self._sphere_x = value
        if self.sphere:
            self.sphere.setPos(self._sphere_x, self._sphere_y, self._sphere_z)

    @property
    def sphere_y(self):
        return self._sphere_y

    @sphere_y.setter
    def sphere_y(self, value):
        self._sphere_y = value
        if self.sphere:
            self.sphere.setPos(self._sphere_x, self._sphere_y, self._sphere_z)

    @property
    def sphere_z(self):
        return self._sphere_z

    @sphere_z.setter
    def sphere_z(self, value):
        self._sphere_z = value
        if self.sphere:
            self.sphere.setPos(self._sphere_x, self._sphere_y, self._sphere_z)

    @property
    def terrain_x(self):
        return self._terrain_x

    @terrain_x.setter
    def terrain_x(self, value):
        self._terrain_x = value
        if self.terrain:
            self.root.setPos(self._terrain_x, self._terrain_y, self._terrain_z)

    @property
    def terrain_y(self):
        return self._terrain_y

    @terrain_y.setter
    def terrain_y(self, value):
        self._terrain_y = value
        if self.terrain:
            self.root.setPos(self._terrain_x, self._terrain_y, self._terrain_z)

    @property
    def terrain_z(self):
        return self._terrain_z

    @terrain_z.setter
    def terrain_z(self, value):
        self._terrain_z = value
        if self.terrain:
            self.root.setPos(self._terrain_x, self._terrain_y, self._terrain_z)

    @property
    def sphere_sz(self):
        return self._sphere_sz

    @sphere_sz.setter
    def sphere_sz(self, value):
        self._sphere_sz = value
        if self.sphere:
            self.sphere.setSz(self._sphere_sz)

    @property
    def sphere_scale(self):
        return self._sphere_scale

    @sphere_scale.setter
    def sphere_scale(self, value):
        self._sphere_scale = value
        if self.sphere:
            self.sphere.setScale(self._sphere_scale)

    def updateLight(self, color, hpr):
        self.render.clearLight()
        if self.scene:
            self.scene.clearLight()
        if self.root:
            self.root.clearLight()
        self.setupLight(color, hpr)

    def setupLight(self, color, hpr):
        sunlight = DirectionalLight("sun")
        sunlight.setColor(color)
        sunlight.setShadowCaster(True, 512, 512)
        self.sunlight = self.render.attachNewNode(sunlight)
        self.sunlight.setHpr(hpr[0], hpr[1], hpr[2])
        self.render.setLight(self.sunlight)
        if self.scene:
            self.scene.setLight(self.sunlight)
        if self.root:
            self.root.setLight(self.sunlight)

    def stop_task(self):
        self.taskMgr.doMethodLater(10, self.stop_camera_spin_task, "stop_task")

    def start_task(self):
        self.taskMgr.doMethodLater(10, self.start_camera_spin_task, "start_task")

    def start_camera_spin_task(self, task):
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        return Task.again

    def stop_camera_spin_task(self, task):
        self.taskMgr.remove("SpinCameraTask")
        return Task.again

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        return Task.cont

    def updateTerrainTask(self, task):
        self.terrain.update()
        return Task.cont


app = MyApp(gui=False)
app.run()
