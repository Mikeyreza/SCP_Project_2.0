import pyglet

class ScreenThree:
    batch = pyglet.graphics.Batch()

    def __init__(self, window):
        self.window = window

        self.bar_height = 30
        self.bar_width = window.width - 80
        self.bar_x = (window.width - self.bar_width) / 2
        self.bar_y = window.height - 100

        self.bar_main_background = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, self.bar_width, self.bar_height,
                                                           color=(50, 50, 50), batch=self.batch)
        self.bar_main_foreground = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, 20, self.bar_height,
                                                           color=(0, 200, 0), batch=self.batch)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()
