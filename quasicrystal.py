# Packages
import math
import random
from PIL import Image

#Set Image Size
imgx = 512; imgy = 512
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()

frequency = random.random() * 50 + 10
phase = random.random() * math.pi
n_rotation = random.randint(10, 20)
print(frequency, phase, n_rotation)

for ky in range(imgy):
    y = float(ky) / (imgy - 1) * 4 * math.pi - 2 * math.pi
    for kx in range(imgx):
        x = float(kx) / (imgx - 1) * 4 * math.pi - 2 * math.pi
        z = 0.0
        for i in range(n_rotation):
            r = math.hypot(x, y)
            a = math.atan2(y, x) + i * math.pi * 2.0 / n_rotation
            z += math.cos(r * math.sin(a) * frequency + phase)
        c = int(round(255 * z / n_rotation))
        pixels[kx, ky] = (c, c, c) # grayscale

image.save("quasicrystal.png", "PNG")
