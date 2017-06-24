#!/usr/bin/python

import time
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 1)
matrix.Clear()


def spiral(n):
    center = (n - 1) / 2

    position = center * (1 + 1j)
    direction = 1
    arm_length = 1
    count = 0

    while True:
        for _ in range(2):
            for _ in range(2):
                for _ in range(arm_length):
                    coords = int(position.real), int(position.imag)
                    yield coords
                    position += direction
                    count += 1
                    if count == n * n:
                        return
                direction *= 1j
            arm_length += 1


def main():
    trail = []
    trail_size = 32

    def display(point):
        trail.append(point)
        while len(trail) > trail_size:
            trail.pop(0)
        # matrix.Clear()
        for i, (x, y) in enumerate(trail):
            fade = 0.2 + 0.8 * (1 + i) * 1.0 / trail_size
            matrix.SetPixel(x, y,
                int(100 * fade),
                int(225 * fade),
                int(255 * fade)
            )
        time.sleep(0.005)

    for point in spiral(32):
        display(point)

    time.sleep(2)
    matrix.Clear()


main()
