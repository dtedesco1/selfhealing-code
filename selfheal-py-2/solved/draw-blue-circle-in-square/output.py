# Step 1
from PIL import Image, ImageDraw
import numpy as np

# Step 2
square_color = np.array([200, 230, 255])
square = np.zeros((500, 500, 3), dtype=np.uint8)
square[:] = square_color

# Step 3
img = Image.fromarray(square)

# Step 4
draw = ImageDraw.Draw(img)

# Step 5
circle_color = (0, 0, 255)
circle_center = (250, 250)
circle_radius = 100
draw.ellipse((circle_center[0]-circle_radius, circle_center[1]-circle_radius, circle_center[0]+circle_radius, circle_center[1]+circle_radius), fill=circle_color)

# Step 6
img.save('output.png')