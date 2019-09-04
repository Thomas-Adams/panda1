from direct.showbase.ShowBase import ShowBase, DirectionalLight, VBase4
from direct.task import Task
from math import pi, sin, cos
from panda3d.core import WindowProperties
import tkinter
from tkinter import *


class MyGui(object):

    def __init__(self, frame, show_base):
        super().__init__()
        self.counter = 0
        self.frame = frame
        self.show_base = show_base
        self._init_menu()
        self.frame.update()
        self.frame.bind('<Configure>', self.on_resize)
        self.init_window_properties()

    def open_camera_controls(self):
        print('Opened Camera controls')
        self.counter += 1
        self.camera_form = Toplevel(self.frame)
        self.camera_form.wm_title('Camera controls')
        self.camera_form.desc = Label(self.camera_form, text="Camera control options").grid(row=0, column=0, sticky=N)
        self.camera_form.desc_angle = Label(self.camera_form, text="Camera angle [degrees]").grid(row=1, column=0,
                                                                                                  sticky=N)
        self.camera_form.angle_slider = Scale(self.camera_form, from_=0, to=359, orient=HORIZONTAL,
                                              command=self.update_camera_angle).grid(row=2, column=0,
                                                                                     sticky=N)
        self.camera_form.desc_x = Label(self.camera_form, text="Camera x-axis").grid(row=3, column=0,
                                                                                     sticky=N)
        self.camera_form.x_axis = Scale(self.camera_form, from_=-200, to=200, orient=HORIZONTAL,
                                        command=self.update_camera_x).grid(row=4, column=0,
                                                                           sticky=N)

        self.camera_form.desc_y = Label(self.camera_form, text="Camera y-axis").grid(row=5, column=0,
                                                                                     sticky=N)
        self.camera_form.y_axis = Scale(self.camera_form, from_=-200, to=200, orient=HORIZONTAL,
                                        command=self.update_camera_y).grid(row=6, column=0,
                                                                           sticky=N)
        self.camera_form.desc_x = Label(self.camera_form, text="Camera x-axis").grid(row=7, column=0,
                                                                                     sticky=N)
        self.camera_form.z_axis = Scale(self.camera_form, from_=-200, to=200, orient=HORIZONTAL,
                                        command=self.update_camera_z).grid(row=8, column=0,
                                                                           sticky=N)
        self.camera_form.desc_red = Label(self.camera_form, text="Light color red channel").grid(row=9, column=0,
                                                                                                 sticky=N)
        self.camera_form.red_scale = Scale(self.camera_form, from_=0, to=1, resolution=0.001, orient=HORIZONTAL,
                                           command=self.update_red_light_color).grid(row=10, column=0,
                                                                                     sticky=N)

        self.camera_form.desc_green = Label(self.camera_form, text="Light color green channel").grid(row=11, column=0,
                                                                                                     sticky=N)
        self.camera_form.green_scale = Scale(self.camera_form, from_=0, to=1, resolution=0.001, orient=HORIZONTAL,
                                             command=self.update_green_light_color).grid(row=12, column=0,
                                                                                         sticky=N)

        self.camera_form.desc_blue = Label(self.camera_form, text="Light color blue channel").grid(row=13, column=0,
                                                                                                   sticky=N)
        self.camera_form.blue_scale = Scale(self.camera_form, from_=0, to=1, resolution=0.001, orient=HORIZONTAL,
                                            command=self.update_blue_light_color).grid(row=14, column=0,
                                                                                       sticky=N)

        self.camera_form.desc_alpha = Label(self.camera_form, text="Light color alpha channel").grid(row=15, column=0,
                                                                                                     sticky=N)
        self.camera_form.alpha_scale = Scale(self.camera_form, from_=0, to=1, resolution=0.001, orient=HORIZONTAL,
                                             command=self.update_alpha_light_color).grid(row=16, column=0,
                                                                                         sticky=N)

        self.camera_form.desc_scene_scale = Label(self.camera_form, text="Scene scale").grid(row=17, column=0,
                                                                                             sticky=N)
        self.camera_form.scene_scale = Scale(self.camera_form, from_=0, to=5, resolution=0.05, orient=HORIZONTAL,
                                             command=self.update_alpha_light_color).grid(row=18, column=0,
                                                                                         sticky=N)

    def update_scene_scale(self, value):
        self.show_base.scene_scale = float(value)

    def update_red_light_color(self, value):
        self.show_base.sun_red = float(value)

    def update_green_light_color(self, value):
        self.show_base.sun_green = float(value)

    def update_blue_light_color(self, value):
        self.show_base.sun_blue = float(value)

    def update_alpha_light_color(self, value):
        self.show_base.sun_alpha = float(value)

    def update_camera_angle(self, value):
        angle = int(value)
        self.show_base.angle_degrees = angle

    def update_camera_x(self, value):
        self.show_base.camera_x = int(value)

    def update_camera_y(self, value):
        self.show_base.camera_y = int(value)

    def update_camera_z(self, value):
        self.show_base.camera_z = int(value)

    def _init_menu(self):
        self.menubar = Menu(self.frame)
        self.frame.config(menu=self.menubar)
        self.controls_menu = Menu(self.menubar)
        self.menubar.add_cascade(label='Controls', menu=self.controls_menu)
        self.controls_menu.add_command(label='Open Camera controls', command=self.open_camera_controls)
        self.controls_menu.add_command(label='Disable mouse', command=self.show_base_disable)
        self.controls_menu.add_command(label='Enable mouse', command=self.show_base_enable)

    def show_base_disable(self):
        self.show_base.disable()

    def show_base_enable(self):
        self.show_base.enable()

    def stop_scene(self):
        if self.show_base:
            self.show_base.stop_task()

    def start_scene(self):
        if self.show_base:
            self.show_base.start_task()

    def init_window_properties(self):
        id = self.frame.winfo_id()
        width = self.frame.winfo_width()
        height = self.frame.winfo_height()
        props = WindowProperties()
        props.setParentWindow(id)
        props.setOrigin(0, 0)
        props.setSize(width, height)

        if self.show_base:
            self.show_base.makeDefaultPipe()
            self.show_base.openDefaultWindow(props=props)
            self.show_base.load_scene()
            self.show_base.run()

    def on_resize(self, event):
        width = self.frame.winfo_width()
        height = self.frame.winfo_height()
        props = WindowProperties()
        props.setSize(width, height)
        # props.setOrigin(0, 0)
        if self.show_base and self.show_base.win:
            self.show_base.win.requestProperties(props)


class MyApp(ShowBase):

    def __init__(self, **kwargs):
        ShowBase.__init__(self, windowType='none')
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
        self._look_at

    def load_scene(self):
        self.scene = self.loader.loadModel("environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        self.camera.setPos(20 * sin(self._angle_radians), -20.0 * cos(self._angle_radians), 3)
        self.setupLight(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha)
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
        self.updateLight()

    @property
    def sun_green(self):
        return self._sun_green

    @sun_green.setter
    def sun_green(self, sun_green):
        self._sun_green = sun_green
        self.updateLight()

    @property
    def sun_blue(self):
        return self._sun_blue

    @sun_blue.setter
    def sun_blue(self, sun_blue):
        self._sun_blue = sun_blue
        self.updateLight()

    @property
    def sun_alpha(self):
        return self._sun_alpha

    @sun_alpha.setter
    def sun_alpha(self, sun_alpha):
        self._sun_alpha = sun_alpha
        self.updateLight()

    @property
    def scene_scale(self):
        return self._scene_scale

    @scene_scale.setter
    def scene_scale(self, scene_scale):
        self._scene_scale = scene_scale
        self.scene.setScale(self._scene_scale, self._scene_scale, self._scene_scale)

    def updateLight(self):
        self.render.clearLight()
        self.setupLight(self._sun_red, self._sun_green, self._sun_blue, self._sun_alpha)

    def setupLight(self, red, green, blue, alpha):
        sunlight = DirectionalLight("sun")
        sunlight.setColor(VBase4(red, green, blue, alpha))
        self.sunlight = self.render.attachNewNode(sunlight)
        self.sunlight.setHpr(45, -60, 0)
        self.render.setLight(self.sunlight)

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
app.startTk()
frame = app.tkRoot
mygui = MyGui(frame, app)
