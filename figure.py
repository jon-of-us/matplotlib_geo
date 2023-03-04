import matplotlib.pyplot as plt
import settings as s
import numpy as np


class Figure:
    def __init__(self, *objects) -> None:
        self.figure = plt.figure("Alle unsere Objekte")
        self.ax = self.figure.add_subplot(111, aspect="equal")
        plt.xlim(-1, 1)  # anpassen der x-Grenzen
        plt.ylim(-1, 1)  # anpassen der y-Grenzen
        self.objects = list(objects)
        self.current_object = None
        self.click_offset = 0j
        self.connect_listeners()

    def init_figure(self):
        self.figure = plt.figure("Alle unsere Objekte")
        self.ax = self.figure.add_subplot(111, aspect="equal")
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

    def connect_listeners(self):
        canvas = self.figure.canvas
        canvas.mpl_connect("button_press_event", self.on_press)
        canvas.mpl_connect("button_release_event", self.on_release)
        canvas.mpl_connect("motion_notify_event", self.on_motion)

    def plot(self):
        pass
        for obj in self.objects:
            obj.clear_artist()
            obj.plot(self.ax)
        self.figure.canvas.draw()

    def on_press(self, event):
        click_pos = event.xdata + 1j * event.ydata
        for obj in self.objects:
            if obj.is_dragable and np.abs(obj() - click_pos) < s.POINT_RADIUS:
                self.current_object = obj
                self.click_offset = obj() - click_pos
                break

    def on_release(self, event):
        self.current_object = None

    def on_motion(self, event):
        if self.current_object == None:
            return
        self.current_object.set_to(event.xdata + 1j * event.ydata)
        self.plot()
