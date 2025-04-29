import pyglet

class ScreenFour:
    batch = pyglet.graphics.Batch()
    background_image = pyglet.resource.image("sheetmetal_fancy.jpg")

    def __init__(self, window):
        self.window = window

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background_image.blit(-280, 0)
            self.batch.draw()

    def update(self, dt):
        print("Updating screen four")