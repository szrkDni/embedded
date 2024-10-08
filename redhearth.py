from sense_hat import SenseHat

sense = SenseHat()

sense.clear()
w = (255, 255, 255) # white
r = (255, 0, 0) # blue

# Set up how the image look like
hearth = [
 w, w, w, w, w, w, w, w,
 w, r, r, w, w, r, r, w,
 r, r, r, r, r, r, r, r,
 r, r, r, r, r, r, r, r,
 w, r, r, r, r, r, r, w,
 w, w, r, r, r, r, w, w,
 w, w, w, r, r, w, w, w,
 w, w, w, w, w, w, w, w]

sense.set_pixels(hearth)