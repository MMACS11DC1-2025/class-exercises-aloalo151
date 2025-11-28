'''
Banana Checker:
Looks at the colour of the banana and judge its ripeness
green = unripe, green-yellow = just ripe, yellow = ripe, yellow-brown = too ripe, brownish = overipe
'''

from PIL import Image

imgList = []

def judgeRipeness(img):
    width = img.width
    height = img.height
    pixels = []
    
    for x in range(width):
        for y in range(height):
            r, g, b = img[x, y]
            if b <= 100:
                pixels.append([x, y, (r, g)])