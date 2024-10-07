from time import sleep
from sense_hat import SenseHat

sense = SenseHat()


# Define the functions
def blinking_hearth():
    b = (0, 0, 0)  # white
    r = (255, 0, 0)  # blue

    hearth = [
        b, b, b, b, b, b, b, b,
        b, r, r, b, b, r, r, b,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        b, r, r, r, r, r, r, b,
        b, b, r, r, r, r, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, b, b, b, b, b]

    count = 0

    while count < 10: #For some reason if it was while True: it didnt stop, neither if the program already did
        sense.set_pixels(hearth)
        sleep(1)
        sense.clear()
        sleep(1)
        count = count +1



def blue():
    sense.clear(0, 0, 255)


def green():
    sense.clear(0, 255, 0)


def yellow():
    sense.clear(255, 255, 0)


sense.stick.direction_up = blinking_hearth
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

while True:

    pass