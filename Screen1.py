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
        self.window.set_location(0,0)

        self.background_image.width = 1300
        self.background_image.height = 700

        self.bar_height = 30
        self.bar_width = window.width - 80
        self.bar_bingus_width = self.bar_width - 350
        self.bar_x = (window.width - self.bar_width) / 2
        self.bar_y = window.height - 100

        self.bar_main_background = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, self.bar_width, self.bar_height,
                                               color=(0, 0, 0), batch=self.batch)
        self.bar_main_foreground = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, 20, self.bar_height,
                             color=(0, 200, 0), batch=self.batch)

        self.bar_one_background = pyglet.shapes.Rectangle(self.bar_x+350, self.bar_y-100, self.bar_width-350, self.bar_height,
                                color=(0, 0, 0), batch=self.batch)
        self.bar_one_foreground = pyglet.shapes.Rectangle(self.bar_x+350, self.bar_y-100, self.bar_width-350, self.bar_height,
                                color=(0, 200, 0), batch=self.batch)

        self.bar_two_background = pyglet.shapes.Rectangle(self.bar_x + 350, self.bar_y - 200, self.bar_width - 350,
                                                          self.bar_height,
                                                          color=(0, 0, 0), batch=self.batch)
        self.bar_two_foreground = pyglet.shapes.Rectangle(self.bar_x + 350, self.bar_y - 200, self.bar_width - 350,
                                                          self.bar_height,
                                                          color=(0, 200, 0), batch=self.batch)

        self.bar_three_background = pyglet.shapes.Rectangle(self.bar_x + 350, self.bar_y - 300, self.bar_width - 350,
                                                          self.bar_height,
                                                          color=(0, 0, 0), batch=self.batch)
        self.bar_three_foreground = pyglet.shapes.Rectangle(self.bar_x + 350, self.bar_y - 300, self.bar_width - 350,
                                                          self.bar_height,
                                                          color=(0, 200, 0), batch=self.batch)

        self.bar_four_background = pyglet.shapes.Rectangle(self.bar_x + 350, self.bar_y - 400, self.bar_width - 350,
                                                          self.bar_height,
                                                          color=(0, 0, 0), batch=self.batch)
        self.bar_four_foreground = pyglet.shapes.Rectangle(self.bar_x + 350, self.bar_y - 400, self.bar_width - 350,
                                                          self.bar_height,
                                                          color=(0, 200, 0), batch=self.batch)

        self.total_label = pyglet.text.Label('Life Support Status',
                                        font_name='Agency FB',
                                        font_size=36,
                                        x=window.width // 2,
                                        y=self.bar_y + self.bar_height + 10,
                                        anchor_x='center',
                                        anchor_y='bottom',
                                        batch=self.batch)

        self.total_label_2 = pyglet.text.Label('Temperature',
                                        font_name='Agency FB',
                                        font_size=30,
                                        x=window.width // 2 + 170,
                                        y=470,
                                        anchor_x='center',
                                        anchor_y='bottom',
                                        batch=self.batch)

        self.total_label_3 = pyglet.text.Label('O2 / CO2 Balance',
                                               font_name='Agency FB',
                                               font_size=30,
                                               x=window.width // 2 + 170,
                                               y=370,
                                               anchor_x='center',
                                               anchor_y='bottom',
                                               batch=self.batch)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background_image.blit(-280, 0)
            self.batch.draw()

    def update_bars(self, dt, speed, score_2, score_3):
        self.progress = (self.progress + speed)
        self.bar_main_foreground.width = (self.progress / 100) * self.bar_width
        self.bar_main_foreground.color = (int(252 - (self.progress / 102) * 252), int((self.progress / 102) * 252), 0)
        if self.bar_main_foreground.width < 0:
            self.bar_main_foreground.width = 0.001
            self.progress = 0
        if self.bar_main_foreground.width > self.bar_width:
            self.bar_main_foreground.width = self.bar_width
            self.progress = 100
        self.bar_one_foreground.width = self.bar_bingus_width * score_2
        self.bar_two_foreground.width = self.bar_bingus_width * score_3
        #print(self.progress, self.speed)

    def increment_speed(self, new_speed):
        self.speed += new_speed

    #pyglet.clock.schedule_interval(update, 1 / 60.0)





