import pyglet
from random import randint
from random import shuffle

class ScreenTwo:
    batch = pyglet.graphics.Batch()
    background_image = pyglet.resource.image("sheetmetal_fancy.jpg")
    question = ""
    answer = 0
    wrong_1 = 0
    wrong_2 = 0
    choices = []
    score = 100

    def __init__(self, window):
        self.window = window
        self.window.set_location(0,710)

        self.score_label = pyglet.text.Label(text="_",
                                             batch=self.batch)

        self.question_label = pyglet.text.Label(text="_",
                                                font_size=30,
                                                font_name="Agency FB",
                                                x=290,
                                                y=500,
                                                batch=self.batch)

        self.screen_button_1 = pyglet.shapes.Rectangle(x=90,
                                                       y=260,
                                                       width=150,
                                                       height=150,
                                                       color=(255, 255, 255, 255),
                                                       batch=self.batch)
        self.answer_label_1 = pyglet.text.Label(text="hi",
                                                x=150,
                                                y=320,
                                                font_size=30,
                                                color=(0, 0, 0, 255),
                                                batch=self.batch)

        self.screen_button_2 = pyglet.shapes.Rectangle(x=315,
                                                       y=260,
                                                       width=150,
                                                       height=150,
                                                       color=(255, 255, 255, 255),
                                                       batch=self.batch)
        self.answer_label_2 = pyglet.text.Label(text="hi",
                                                x=375,
                                                y=320,
                                                font_size=30,
                                                color=(0, 0, 0, 255),
                                                batch=self.batch)

        self.screen_button_3 = pyglet.shapes.Rectangle(x=540,
                                                       y=260,
                                                       width=150,
                                                       height=150,
                                                       color=(255, 255, 255, 255),
                                                       batch=self.batch)
        self.answer_label_3 = pyglet.text.Label(text="hi",
                                                x=600,
                                                y=320,
                                                font_size=30,
                                                color=(0, 0, 0, 255),
                                                batch=self.batch)

        self.total_label = pyglet.text.Label('Temperature',
                                        font_name='Agency FB',
                                        font_size=36,
                                        x=window.width // 2,
                                        y=580,
                                        anchor_x='center',
                                        anchor_y='bottom',
                                        batch=self.batch)

        self.accuracy_label = pyglet.text.Label(text="_",
                                                font_name="Agency FB",
                                                font_size=50,
                                                x=window.width//2,
                                                y=100,
                                                anchor_x='center',
                                                anchor_y='bottom',
                                                batch=self.batch)

        self.background_image.width = 1300
        self.background_image.height = 700

        @self.window.event
        def on_draw():
            self.window.clear()
            self.background_image.blit(-280, 0)
            self.batch.draw()

    def generate_question(self):
        operation = randint(1, 4)
        if operation == 1:
            number_1 = randint(1, 100)
            number_2 = randint(1, 100)
            self.question = f"{number_1} + {number_2}"
            self.answer = number_1 + number_2
        elif operation == 2:
            number_1 = randint(51, 100)
            number_2 = randint(1, 50)
            self.question = f"{number_1} - {number_2}"
            self.answer = number_1 - number_2
        elif operation == 3:
            number_2 = randint(1, 10)
            self.answer = randint(1, 10)
            number_1 = number_2 * self.answer
            self.question = f"{number_1} ÷ {number_2}"
        elif operation == 4:
            number_1 = randint(1, 10)
            number_2 = randint(1, 10)
            self.question = f"{number_1} x {number_2}"
            self.answer = number_1 * number_2
        else:
            self.generate_question()
        self.wrong_1 = self.answer + randint(1, 10)
        self.wrong_2 = self.answer - randint(1, 10)
        self.choices = [self.answer, self.wrong_1, self.wrong_2]
        shuffle(self.choices)
        self.answer_label_1.text = str(self.choices[0])
        self.answer_label_2.text = str(self.choices[1])
        self.answer_label_3.text = str(self.choices[2])
        self.question_label.text = self.question + " equals ?"
        
    def check_input(self, button):
        choice = self.choices[button]
        if self.score == 100:
            self.accuracy_label.text = "Maximum score reached!"
            return
        if choice == self.answer:
            self.accuracy_label.text = "Correct!"
            self.accuracy_label.color = (0, 255, 0, 255)
            self.score += 1
            ScreenTwo.generate_question(self)
        else:
            self.accuracy_label.color = (255, 0, 0, 255)
            self.accuracy_label.text = "Incorrect!"

    def game_event(self, dt):
        self.score_label.text = str(self.score)
        if self.score < 100:
            return
        rand = randint(1, 5)
        print(rand)
        if rand == 3:
            self.score = 0
            self.generate_question()
            self.accuracy_label.text = "ATTENTION NEEDED!"
            self.accuracy_label.color = (255, 0, 0, 255)

    def return_score(self):
        return self.score / 100
