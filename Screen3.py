import pyglet
from random import randint

class ScreenThree:
    batch = pyglet.graphics.Batch()
    background_image = pyglet.resource.image("sheetmetal_fancy.jpg")
    water_level = 100

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
        self.window.set_location(768, 0)

        self.module_label = pyglet.text.Label('O2 and CO2 Control',
                                             font_name='Agency FB',
                                             font_size=36,
                                             x=window.width // 2,
                                             y=580,
                                             anchor_x='center',
                                             anchor_y='bottom',
                                             batch=self.batch)

        self.description_label = pyglet.text.Label(text="Water the plant to keep your O2 and CO2 levels balanced!",
                                                font_size=30,
                                                font_name="Agency FB",
                                                x=25,
                                                y=500,
                                                batch=self.batch)

        self.warning_label = pyglet.text.Label(text="_",
                                                font_name="Agency FB",
                                                font_size=50,
                                                x=window.width // 2,
                                                y=100,
                                                anchor_x='center',
                                                anchor_y='bottom',
                                                batch=self.batch)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background_image.blit(-280, 0)
            self.render_plant().blit(100, 200)
            self.batch.draw()

    def render_plant(self):
        if self.water_level < 33:
            return self.plant_images[2]
        if self.water_level < 66:
            return self.plant_images[1]
        if self.water_level < 101:
            self.warning_label.text = " "
            return self.plant_images[0]

    def water_plant(self):
        if self.water_level == 100:
            return self.water_level
        self.water_level += 2
        if self.water_level > 100:
            self.water_level = 100
        return self.water_level

    def game_event(self, dt):
        if self.water_level < 100:
            return
        rand = randint(1, 5)
        if rand == 3:
            self.water_level -= 50
            self.warning_label.text = "ATTENTION NEEDED!"
            self.warning_label.color = (255, 0, 0, 255)

    def update(self, dt):
        print("Updating screen three")

    def return_score(self):
        return self.water_level / 100