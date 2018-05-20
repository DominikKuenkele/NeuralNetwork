import numpy
import matplotlib.pyplot

from PIL import Image
im = Image.open("hsf_0_00000.png")

from numpy.ma import greater

greyscale = numpy.zeros([128, 128])

for y in range(128):
    for x in range(128):
        r, g, b = im.getpixel((y, x))
        greyscale[x, y] = (((r + g + b) / 3) / 255 * 0.99) + 0.01

matplotlib.pyplot.imshow(greyscale, cmap='Greys', interpolation='none')
# numpy.set_printoptions(threshold='nan')
# print(greyscale)