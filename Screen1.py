import pyglet

class ScreenOne:
    batch = pyglet.graphics.Batch()

    def __init__(self, difficulty):
        self.height = 640
        self.width = 768

        self.difficulty = difficulty

        self.bar_height = 30
        self.bar_width = self.width - 80
        self.bar_x = (self.width - self.bar_width) / 2
        self.bar_y = self.height - 100

        self.window = pyglet.window.Window(height=self.height, width=self.width)
        self.window.set_location(0, 0)

        self.bar_main_background = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, self.bar_width, self.bar_height,
                                               color=(50, 50, 50), batch=self.batch)
        self.bar_main_foreground = pyglet.shapes.Rectangle(self.bar_x, self.bar_y, 20, self.bar_height,
                             color=(0, 200, 0), batch=self.batch)


        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()



