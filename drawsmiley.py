from sense_hat import SenseHat
import random

sense = SenseHat()


sense.clear()


def random_colour():
# randint - random integer between an interval
   random_red = random.randint(0, 255)
   random_green = random.randint(0, 255)
   random_blue = random.randint(0, 255)
   return (random_red, random_green, random_blue)


def set_mouth(colour):
    sense.set_pixel(1, 5, colour)
    sense.set_pixel(1, 6, colour)
    sense.set_pixel(2, 5, colour)
    sense.set_pixel(2, 6, colour)
    sense.set_pixel(3, 6, colour)
    sense.set_pixel(4, 6, colour)
    sense.set_pixel(5,6,colour)
    sense.set_pixel(5,5,colour)
    sense.set_pixel(6,6,colour)
    sense.set_pixel(6,5,colour)

def set_eye(x,y,colour):
    sense.set_pixel(x, y, colour)
    sense.set_pixel(x, y+1, colour)
    sense.set_pixel(x+1, y, colour)
    sense.set_pixel(x+1, y+1, colour)

def draw_smiley():
    set_eye(1,1,random_colour())
    set_eye(5,1,random_colour())
    set_mouth(random_colour())

def main():
    draw_smiley()


main()