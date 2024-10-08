from sense_hat import SenseHat

sense = SenseHat()

sense.clear()
w = (255, 255, 255) # white
b = (0, 0, 255) # blue

# Set up how the image look like
smiley_pixels = [
 w, w, w, w, w, w, w, w,
 w, b, b, w, w, b, b, w,
 w, b, b, w, w, b, b, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, b, w, w, w, w, b, w,
 w, w, b, b, b, b, w, w,
 w, w, w, w, w, w, w, w]

sense.set_pixels(smiley_pixels)