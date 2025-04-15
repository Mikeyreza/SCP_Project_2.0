import pyglet
import Screen1
import Screen2
import Screen3
from pyglet.window import key

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

window_3 = pyglet.window.Window(height=640, width=768, caption="Screen Three")

Screen3 = Screen3.ScreenThree(window_3)

pyglet.app.run()