from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()
b = (0, 0, 0)
f = (255, 0, 0)


right_arrow = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, f, b, b, b,
    b, b, b, b, b, f, b, b,
    b, f, f, f, f, f, f, b,  # Up arrow
    b, b, b, b, b, f, b, b,
    b, b, b, b, f, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

def arrow_pattern():
    up = [
        b, b, b, b, b, b, b, b,
        b, b, b, f, b, b, b, b,
        b, b, f, f, f, b, b, b,
        b, f, b, f, b, f, b, b, #Up arrow
        b, b, b, f, b, b, b, b,
        b, b, b, f, b, b, b, b,
        b, b, b, f, b, b, b, b,
        b, b, b, b, b, b, b, b]


    return up


pixels = arrow_pattern()

while True:
    # go throw all joystick’s events
    for event in sense.stick.get_events():
        # Check if the joystick was pressed

        if event.action == "pressed":
            # Check which direction
            sense.set_rotation(0)

            if event.direction == "up":
                sense.set_pixels(pixels)
            elif event.direction == "down":
                sense.set_pixels(pixels)
                sense.flip_v()
            elif event.direction == "left":
                sense.set_rotation(270)
                sense.set_pixels(pixels)
            elif event.direction == "right":
                sense.set_rotation(90)
                sense.set_pixels(pixels)
                sense.flip_h()# Right arrow



            # Wait a while and then clear the screen
            sleep(0.5)
            sense.clear()
