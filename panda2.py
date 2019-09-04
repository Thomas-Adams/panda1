from direct.showbase.ShowBase import ShowBase, DirectionalLight, VBase4, TextNode
from direct.gui.DirectGui import *
from direct.task import Task
from math import pi, sin, cos
from panda3d.core import WindowProperties

UPPER_POS_LIMIT = 1000
LOWER_POS_LIMIT = -1000
COLOR_RANGE = (0, 1)

POS_RANGE = (LOWER_POS_LIMIT, UPPER_POS_LIMIT)
ANGLE_RANGE = (-360, 360)

LABEL_FG = (1, 1, 1, 1)
LABEL_BG = (0, 0, 0, 1)


class MyGUI(object):

    def __init__(self, show_base):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1),
                                 frameSize=(-1, 1, -1, 1),
                                 pos=(1, -1, -1))
        self.slider_camera_x = DirectSlider(parent=self.frame, range=POS_RANGE, value=0, pageSize=0.1,
                                            command=self.update_camera_x)
        self.slider_camera_x.setScale(0.2)
        self.slider_camera_x.setPos(-0.5, 0.0, 0.95)

        self.label_camera_x = DirectLabel(parent=self.frame, text='Camera x-axis')
        self.label_camera_x.setScale(0.03)
        self.label_camera_x.setPos(-0.85, 0.0, 0.95)

        self.slider_camera_y = DirectSlider(parent=self.frame, range=POS_RANGE, value=0, pageSize=0.1,
                                            command=self.update_camera_y)
        self.slider_camera_y.setScale(0.2)
        self.slider_camera_y.setPos(-0.5, 0, 0.85)

        self.label_camera_y = DirectLabel(parent=self.frame, text='Camera y-axis')
        self.label_camera_y.setScale(0.03)
        self.label_camera_y.setPos(-0.85, -1, 0.85)

        self.slider_camera_z = DirectSlider(parent=self.frame, range=POS_RANGE, value=0, pageSize=0.1,
                                            command=self.update_camera_z)
        self.slider_camera_z.setScale(0.2)
        self.slider_camera_z.setPos(-0.5, 0, 0.75)

        self.label_camera_z = DirectLabel(parent=self.frame, text='Camera z-axis')
        self.label_camera_z.setScale(0.03)
        self.label_camera_z.setPos(-0.85, 0, 0.75)

        self.slider_camera_heading = DirectSlider(parent=self.frame, range=(-360, 360), value=0, pageSize=0.1,
                                                  command=self.update_camera_heading)
        self.slider_camera_heading.setScale(0.2)
        self.slider_camera_heading.setPos(-0.5, 0, 0.65)

        self.label_camera_heading = DirectLabel(parent=self.frame, text='Camera heading')
        self.label_camera_heading.setScale(0.03)
        self.label_camera_heading.setPos(-0.85, 0, 0.65)

        self.slider_camera_pitch = DirectSlider(parent=self.frame, range=(-360, 360), value=0, pageSize=0.1,
                                                command=self.update_camera_pitch)
        self.slider_camera_pitch.setScale(0.2)
        self.slider_camera_pitch.setPos(-0.5, 0, 0.55)

        self.label_camera_pitch = DirectLabel(parent=self.frame, text='Camera pitch')
        self.label_camera_pitch.setScale(0.03)
        self.label_camera_pitch.setPos(-0.85, 0, 0.55)

        self.slider_camera_roll = DirectSlider(parent=self.frame, range=(-360, 360), value=0, pageSize=0.1,
                                               command=self.update_camera_roll)
        self.slider_camera_roll.setScale(0.2)
        self.slider_camera_roll.setPos(-0.5, 0, 0.45)

        self.label_camera_roll = DirectLabel(parent=self.frame, text='Camera roll')
        self.label_camera_roll.setScale(0.03)
        self.label_camera_roll.setPos(-0.85, 0, 0.45)

        self.slider_sun_red = DirectSlider(parent=self.frame, range=COLOR_RANGE, value=0.92, pageSize=0.01,
                                           command=self.update_sun_red)
        self.slider_sun_red.setScale(0.2)
        self.slider_sun_red.setPos(-0.5, 0, 0.35)

        self.label_sun_red = DirectLabel(parent=self.frame, text='Light red channel')
        self.label_sun_red.setScale(0.03)
        self.label_sun_red.setPos(-0.85, 0, 0.35)

        self.slider_sun_green = DirectSlider(parent=self.frame, range=COLOR_RANGE, value=0.91, pageSize=0.01,
                                             command=self.update_sun_green)
        self.slider_sun_green.setScale(0.2)
        self.slider_sun_green.setPos(-0.5, 0, 0.25)

        self.label_sun_green = DirectLabel(parent=self.frame, text='Light green channel')
        self.label_sun_green.setScale(0.03)
        self.label_sun_green.setPos(-0.85, 0, 0.25)

        self.slider_sun_blue = DirectSlider(parent=self.frame, range=COLOR_RANGE, value=0.91, pageSize=0.01,
                                            command=self.update_sun_blue)
        self.slider_sun_blue.setScale(0.2)
        self.slider_sun_blue.setPos(-0.5, 0, 0.15)

        self.label_sun_blue = DirectLabel(parent=self.frame, text='Light blue channel')
        self.label_sun_blue.setScale(0.03)
        self.label_sun_blue.setPos(-0.85, 0, 0.15)

        self.slider_sun_yaw = DirectSlider(parent=self.frame, range=ANGLE_RANGE, value=0.0, pageSize=0.1,
                                           command=self.update_sun_yaw)
        self.slider_sun_yaw.setScale(0.2)
        self.slider_sun_yaw.setPos(0.2, 0, 0.95)

        self.label_sun_yaw = DirectLabel(parent=self.frame, text='Light yaw')
        self.label_sun_yaw.setScale(0.03)
        self.label_sun_yaw.setPos(-0.15, 0, 0.95)

        self.slider_sun_pitch = DirectSlider(parent=self.frame, range=ANGLE_RANGE, value=0.0, pageSize=0.1,
                                             command=self.update_sun_pitch)
        self.slider_sun_pitch.setScale(0.2)
        self.slider_sun_pitch.setPos(0.2, 0, 0.85)

        self.label_sun_pitch = DirectLabel(parent=self.frame, text='Light pitch')
        self.label_sun_pitch.setScale(0.03)
        self.label_sun_pitch.setPos(-0.15, 0, 0.85)

        self.slider_sun_roll = DirectSlider(parent=self.frame, range=ANGLE_RANGE, value=0.0, pageSize=0.1,
                                            command=self.update_sun_roll)
        self.slider_sun_roll.setScale(0.2)
        self.slider_sun_roll.setPos(0.2, 0, 0.75)

        self.label_sun_roll = DirectLabel(parent=self.frame, text='Light roll')
        self.label_sun_roll.setScale(0.03)
        self.label_sun_roll.setPos(-0.15, 0, 0.75)

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


class MyApp(ShowBase):

    def __init__(self, **kwargs):
        ShowBase.__init__(self)
        self._angle_degrees = 30
        self._angle_radians = self._angle_degrees * (pi / 180.0)
        self._camera_x = 0
        self._camera_y = 0
        self._camera_z = 0
        self._sun_red = 0.92
        self._sun_green = 0.91
        self._sun_blue = 0.91
        self._sun_alpha = 1
        self._scene_scale = 0.25
        self._light_yaw = 0
        self._light_pitch = -60
        self._light_roll = 0
        self._camera_heading = 0
        self._camera_pitch = 0
        self._camera_roll = 0

        self.load_scene()
        self.handler = MyGUI(self)

    def load_scene(self):
        self.scene = self.loader.loadModel("environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        self.camera.setPos(0, 0, 0)
        self.setupLight(VBase4(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha),
                        (self._light_yaw, self._light_pitch, self._light_roll))
        self.render.setShaderAuto()
        self.disable()

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

    def updateLight(self, color, hpr):
        self.render.clearLight()
        self.scene.clearLight()
        self.setupLight(color, hpr)

    def setupLight(self, color, hpr):
        sunlight = DirectionalLight("sun")
        sunlight.setColor(color)
        sunlight.setShadowCaster(True, 512, 512)
        self.sunlight = self.render.attachNewNode(sunlight)
        self.sunlight.setHpr(hpr[0], hpr[1], hpr[2])
        self.render.setLight(self.sunlight)
        self.scene.setLight(self.sunlight)

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


app = MyApp()
app.run()
