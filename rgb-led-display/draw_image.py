#!/usr/bin/python

import Image
import ImageDraw
import signal
import sys
import time
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 1)


def signal_handler(signal, frame):
    matrix.Clear()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def draw_animated(filename):
    image = Image.open(filename)
    duration = image.info.get("duration", 30) / 1000.0
    while True:
        image.load()          # Must do this before SetImage() calls
        matrix.SetImage(image.im.id, 0, 0)
        time.sleep(duration)
        try:
            image.seek(image.tell() + 1)
        except:
            matrix.Clear()
            return


while True:
    for filename in sys.argv[1:]:
        print filename
        draw_animated(filename)
