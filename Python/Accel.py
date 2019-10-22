# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the LSM303 module.
import Adafruit_LSM303


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
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.

# Load default font.
font = ImageFont.load_default()

# "True" is to turn dark mode on, "False" is to turn it off
Dark_Mode = True
bgcol = 0
txtcol = 255

if Dark_Mode == False:
    bgcol = 0
    txtcol = 255
else:
    bgcol = 255
    txtcol = 0

while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    x = int(accel_x) * (9.81/1024)
    y = int(accel_y) * (9.81/1024)
    z = int(accel_z) * (9.81/1024)

    x = round(x, 3)
    y = round(y, 3)
    z = round(z, 3)

    # Write the text.
    draw.rectangle((0,0,width,height), outline=0, fill= int(bgcol))
    draw.text((5, top),    'Accelerometer Data:',  font=font, fill= int(txtcol))
    draw.text((5, top+20), 'X: '+str(x)+' m/s' + u"\u00B2", font=font, fill= int(txtcol))
    draw.text((5, top+35), 'Y: '+str(y)+' m/s' + u"\u00B2", font=font, fill= int(txtcol))
    draw.text((5, top+50), 'Z: '+str(z)+' m/s' + u"\u00B2", font=font, fill= int(txtcol))
    
    # Display image.
    disp.image(image)
    disp.display()

    time.sleep(0.5)
