from time import sleep
from sense_hat import SenseHat
import random

sense = SenseHat()

sense.clear()

o = (0, 0, 0)
b = (0, 0, 255)

one_img = \
    [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o]

two_img = \
    [
        b, b, o, o, o, o, o, o,
        b, b, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, b, b,
        o, o, o, o, o, o, b, b]

three_img = \
    [
        b, b, o, o, o, o, o, o,
        b, b, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, b, b,
        o, o, o, o, o, o, b, b]

four_img = \
    [
        b, b, o, o, o, o, b, b,
        b, b, o, o, o, o, b, b,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        b, b, b, o, o, o, b, b,
        b, b, o, o, o, o, b, b]

five_img = \
    [
        b, b, o, o, o, o, b, b,
        b, b, o, o, o, o, b, b,
        o, o, o, o, o, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, b, b, o, o, o,
        o, o, o, o, o, o, o, o,
        b, b, o, o, o, o, b, b,
        b, b, o, o, o, o, b, b]

six_img = \
    [
        b, b, o, o, o, o, b, b,
        b, b, o, o, o, o, b, b,
        o, o, o, o, o, o, o, o,
        b, b, o, o, o, o, b, b,
        b, b, o, o, o, o, b, b,
        o, o, o, o, o, o, o, o,
        b, b, b, o, o, o, b, b,
        b, b, o, o, o, o, b, b]


# print(str(intro_numbers))

def simulate_drawing(event):
    print(intro_numbers)
    for i in range(len(intro_numbers)):
        if intro_numbers[i] == 1:
            sense.set_pixels(one_img)
        elif intro_numbers[i] == 2:
            sense.set_pixels(two_img)
        elif intro_numbers[i] == 3:
            sense.set_pixels(three_img)
        elif intro_numbers[i] == 4:
            sense.set_pixels(four_img)
        elif intro_numbers[i] == 5:
            sense.set_pixels(five_img)
        elif intro_numbers[i] == 6:
            sense.set_pixels(six_img)
        sleep(.1)


def show_generated_number():
    val = random.randint(1, 6)

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
        sense.set_pixels(six_img)


count = 0

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            intro_numbers = [random.randint(1, 6) for i in range(10)]
            simulate_drawing(event)

            sense.clear()
            sleep(.8)

            show_generated_number()

            count += 1
