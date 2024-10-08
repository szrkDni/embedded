from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()
b = (0, 0, 0)
f = (255, 0, 0)




right_arrow = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, f, b, b, b,
    b, b, b, b, b, f, b, b,
    b, f, f, f, f, f, f, b,  # Right arrow
    b, b, b, b, b, f, b, b,
    b, b, b, b, f, b, b, b,
    b, b, b, b, b, b, b, b

]

up_arrow = [
        b, b, b, b, b, b, b, b,
        b, b, b, f, b, b, b, b,
        b, b, f, f, f, b, b, b,
        b, f, b, f, b, f, b, b, #Up arrow
        b, b, b, f, b, b, b, b,
        b, b, b, f, b, b, b, b,
        b, b, b, f, b, b, b, b,
        b, b, b, b, b, b, b, b]


while True:
    # go throw all joystick’s events
    for event in sense.stick.get_events():
        # Check if the joystick was pressed

        if event.action == "pressed":
            # Check which direction

            if event.direction == "up":
                sense.set_pixels(up_arrow)
            elif event.direction == "down":
                sense.set_pixels(up_arrow)
                sense.flip_v()
            elif event.direction == "left":
                sense.set_pixels(right_arrow)
                sense.flip_h()
            elif event.direction == "right":
                sense.set_pixels(right_arrow)




            # Wait a while and then clear the screen
            sleep(0.5)
            sense.clear()