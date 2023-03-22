import numpy as np
from PIL import Image, ImageDraw

# create the expected numpy array for the square
square_color = np.array([200, 230, 255])
square = np.zeros((500, 500, 3), dtype=np.uint8)
square[:] = square_color

# create the expected Image object for the square
expected_img = Image.fromarray(square)

# draw the expected circle on the expected Image object
draw = ImageDraw.Draw(expected_img)
circle_color = (0, 0, 255)
circle_center = (250, 250)
circle_radius = 100
draw.ellipse((circle_center[0]-circle_radius, circle_center[1]-circle_radius, circle_center[0]+circle_radius, circle_center[1]+circle_radius), fill=circle_color)

# save the expected Image object to a file
expected_img.save('expected_output.png')

# run the code that should generate the output
exec(open('output.py').read())

# ensure that the generated output is equal to the expected output
generated_img = Image.open('output.png')
assert np.array_equal(np.array(generated_img), np.array(expected_img))