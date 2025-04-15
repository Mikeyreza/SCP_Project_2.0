from xml.etree.ElementTree import tostring

import pyglet
from pyglet.window import key
from pyglet.window.key import KeyStateHandler


class ScreenOne:
    batch = pyglet.graphics.Batch()
    background_image = pyglet.resource.image("sheetmetal_fancy.jpg")

    def __init__(self, window):
        self.progress = 0
        self.speed = 0

        self.window = window

        self.background_image.width = 1300
        self.background_image.height = 700

        self.bar_height = 30
        self.bar_width = window.width - 80
        self.bar_x = (window.width - self.bar_width) / 2
        self.bar_y = window.height - 100

        self.bar_main_background = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, self.bar_width, self.bar_height,
                                               color=(0, 0, 0), batch=self.batch)
        self.bar_main_foreground = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, 20, self.bar_height,
                             color=(0, 200, 0), batch=self.batch)

        self.total_label = pyglet.text.Label('Life Support Status',
                                        font_name='Agency FB',
                                        font_size=36,
                                        x=window.width // 2,
                                        y=self.bar_y + self.bar_height + 10,
                                        anchor_x='center',
                                        anchor_y='bottom',
                                        batch=self.batch)

        @window.event
        def on_draw():
            self.window.clear()
            self.background_image.blit(-280, 0)
            self.update_bars()
            self.batch.draw()

    def update_bars(self):
        self.progress = (self.progress + self.speed)
        self.bar_main_foreground.width = (self.progress / 100) * self.bar_width
        self.bar_main_foreground.color = (int(252 - (self.progress / 102) * 252), int((self.progress / 102) * 252), 0)
        if self.bar_main_foreground.width < 0:
            self.bar_main_foreground.width = 0.001
            self.progress = 0
        if self.bar_main_foreground.width > self.bar_width:
            self.bar_main_foreground.width = self.bar_width
            self.progress = 100
        #print(self.progress, self.speed)

    def increment_speed(self, new_speed):
        self.speed += new_speed

    #pyglet.clock.schedule_interval(update, 1 / 60.0)





