from PIL import Image

mac = Image.open('pictures/example.jpg')
mac.size
mac.filename

# Cropping Images
mac.crop((0, 0, 100, 100))
pencils = Image.open('pictures/pencils.jpg')

# Bottom pencils
x = 0
y = 0

w = 1950 / 3
h = 1300

pencils.crop(x, y, w, h)

# Color transparency
red = Image.open('pictures/red_color.jpg')
blue = Image.open('pictures/blue_color.png')
blue.putalpha(182)
