from time import sleep
from sense_hat import SenseHat
import random

sense = SenseHat()

o = (0,0,0) #no color
b = (0,0,255)

one_img = \
    [o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o]



two_img = \
    [o,o,o,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

three_img = \
    [o,o,o,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,o,o,o]


four_img = \
    [o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

five_img = \
    [o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

six_img = []

def number_gen(event):
    if event.action == "pressed":
        val = random.randint(1,6)
        print(val)
        if val == 1:
            sense.set_pixels(one_img)
        elif val == 2:
            sense.set_pixels(two_img)
        elif val == 3:
            sense.set_pixels(three_img)
        elif val == 4:
            sense.set_pixels(four_img)
        elif val == 5:
            sense.set_pixels(five_img)
        elif val == 6:
            print(6)
        sleep(2)
        sense.clear()




while True:
    for event in sense.stick.get_events():
        number_gen(event)

    sleep(2)
    sense.clear()