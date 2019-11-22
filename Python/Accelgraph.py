import time

# Import the LSM303 module.
import Adafruit_LSM303
import math

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
scrnwidth = disp.width
scrnheight = disp.height
image = Image.new('1', (scrnwidth, scrnheight))
image2 = Image.new('1', (scrnwidth, scrnheight))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = scrnheight-padding
# Move left to right keeping track of the current x position for drawing shapes.

# Load default font.
font = ImageFont.load_default()

# "True" is to turn dark mode on, "False" is to turn it off
Dark_Mode = False
bgcol = 0
txtcol = 255

# screen dimensions: 128 x 64 pixels

if Dark_Mode == False:
    bgcol = 0
    txtcol = 255
else:
    bgcol = 255
    txtcol = 0

points = [0,0]
a = 1
x = 0
y = 0
l = 0
X = 0
z = 1
while True:
    draw.rectangle((0,0,scrnwidth,scrnheight), outline= int(bgcol), fill= int(bgcol))
    
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

#    x = int(accel_x) * (9.81/1024)
 #   y = int(accel_y) * (9.81/1024)
    z = int(accel_z) * (9.81/1024)

 #   x = round(x, 3)
  #  y = round(y, 3)
    z = round(z, 3)

    z = z * 2

    points.insert(0, z)

    l = len(points)
    if l == 56:
        points.pop(55)
    
    # Write the text.
    draw2.text((80, 0), 'a (m/s' + u"\u00B2" + ')', font=font, fill= int(txtcol))
    w = image2.rotate(90, expand=1)
    image.paste(w)
    draw.text((50, 54), 't (s)',  font=font, fill= int(txtcol))
    
    for v in points:
        y = 49 - int(v)
        X = x + 14
        draw.point((X, y), fill= (txtcol))
        x = x + 2
        #disp.image(image)
        #disp.display()

    draw.line((13,0,13,49), fill= int(txtcol))
    draw.line((14,49,127,49), fill= int(txtcol))

    # Display image.
    disp.image(image)
    disp.display()

    x = 0
