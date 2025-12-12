from PIL import Image
import time

bird = Image.open("5.5/Major_Mitchell's_Cockatoo_-_Mt_Grenfell.jpg")

height = bird.height
width = bird.width

bird = bird.load()

brightness = 0
timerStart = time.time()
for y in range(height):
    for x in range(width):
        r, g, b = bird[x, y]
        brightness += (r+g+b)/3
endTime = time.time() - timerStart     
print(height*width*255) 
print(brightness)
brightness = brightness/(height*width*255)*100

print(f"This image is {brightness:.2f}% bright (0 is black/dark, 100 is white/bright)")
print(f"This took {endTime:.3f} seconds")