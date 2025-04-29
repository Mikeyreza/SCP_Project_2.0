import pyglet

class ScreenThree:
    batch = pyglet.graphics.Batch()
    background_image = pyglet.resource.image("sheetmetal_fancy.jpg")
    water_level = 0

    plant_images = [
        pyglet.resource.image("plant_p1.png"),
        pyglet.resource.image("plant_p2.png"),
        pyglet.resource.image("plant_p3.png"),
    ]

    for plant in plant_images:
        plant.width = 200
        plant.height = 250

    def __init__(self, window):
        self.window = window

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background_image.blit(-280, 0)
            self.render_plant().blit(100, 100)
            self.batch.draw()

    def render_plant(self):
        if self.water_level < 33:
            return self.plant_images[2]
        if self.water_level < 66:
            return self.plant_images[1]
        if self.water_level < 101:
            return self.plant_images[0]

    def water_plant(self):
        if self.water_level == 100:
            return self.water_level
        self.water_level += 2
        if self.water_level > 100:
            self.water_level = 100
        return self.water_level

    def update(self, dt):
        print("Updating screen three")
