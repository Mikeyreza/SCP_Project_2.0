import pyglet
import Screen1
import Screen2
import Screen3
import Screen4
from random import randint
from pyglet.window import key
#from gpiozero import Button

window_1 = pyglet.window.Window(height=640, width=768, caption="Screen One")

Screen1 = Screen1.ScreenOne(window_1)

window_2 = pyglet.window.Window(height=640, width=768, caption="Screen Two")

Screen2 = Screen2.ScreenTwo(window_2)

@window_2.event
def on_key_press(symbol, modifiers):
    if symbol == key.B:
        Screen1.increment_speed(1)
    if symbol == key.N:
        Screen1.increment_speed(-1)
    if symbol == key.G:
        Screen2.generate_question()
    if symbol == key.C:
        Screen2.check_input(1)
    if symbol == key.LEFT:
        button_1_func()
    if symbol == key.DOWN:
        button_2_func()
    if symbol == key.RIGHT:
        button_3_func()
    if symbol == key.W:
        button_4_func()

def button_1_func():
    print("Button 1 pressed!")
    Screen2.check_input(0)

def button_2_func():
    print("Button 2 pressed!")
    Screen2.check_input(1)
    
def button_3_func():
    print("Button 3 pressed!")
    Screen2.check_input(2)

def button_4_func():
    print("Button 4 pressed!")
    Screen3.water_plant()
'''
button_1 = Button(13)
button_2 = Button(19)
button_3 = Button(26)
button_4 = Button(6)

button_1.when_pressed = button_1_func
button_2.when_pressed = button_2_func
button_3.when_pressed = button_3_func
button_4.when_pressed = button_4_func
'''
Screen2.generate_question()

window_3 = pyglet.window.Window(height=640, width=768, caption="Screen Three")

Screen3 = Screen3.ScreenThree(window_3)

#pyglet.clock.schedule_interval(Screen3.update, 1/60)

window_4 = pyglet.window.Window(height=640, width=768, caption="Screen Four")

Screen4 = Screen4.ScreenFour(window_4)

#pyglet.clock.schedule_interval(Screen4.update, 1/60)


def calculate_score(dt):
    score_2 = Screen2.return_score()
    score_3 = Screen3.return_score()
    total_score = (score_2+score_3/2)-0.5
    Screen1.update_bars(1, total_score, score_2, score_3)

pyglet.clock.schedule_interval(calculate_score, 1/60)

#pyglet.clock.schedule_interval(Screen1.update_bars, 1/60, total_score)

pyglet.clock.schedule_interval(Screen2.game_event, 1)

pyglet.clock.schedule_interval(Screen3.game_event, 1)

pyglet.app.run()