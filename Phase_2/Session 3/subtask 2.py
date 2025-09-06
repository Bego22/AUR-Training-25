import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

img = cv2.imread('shapes.jpg')


out = img.copy() # type: ignore
# Make a mask for each color (red, blue, black)
# Take care that the default colorspace that OpenCV opens an image in is BGR not# RGB
# Change all pixels that fit within the blue mask to black
# Change all pixels that fit within the red mask to blue
# Change all pixels that fit within the black mask to red

height , width , rgb = out.shape
""""
for i in range(height):
    for j in range(width):
        b,g,r = out[i,j]
        if ( b >= 100 ) and ( g <= 100) and ( r <= 100 ) :#BLUE
            out[i,j] = [0,0,0]
        elif (b <= 100) and ( g<= 100) and ( r >= 100) : #RED
            out[i][j] = [255,0,0]

        elif ( b == 0) and ( g == 0) and ( r == 0) : #BLACK
            out[i][j] = [0,0,255]

    """
blue_mask = (out[: ,: , 0] >= 100) & (out[: , : , 1] <= 100) & (out[: , : , 2] <= 100)
red_mask = (out[: ,: , 0] <= 100) & (out[: , : , 1] <= 100) & (out[: , : , 2] >= 100)
black_mask = (out[: ,: , 0] == 0) & (out[: , : , 1] == 0) & (out[: , : , 2] == 0)


out[blue_mask] = [0,0,0]
out[red_mask] = [255,0,0]
out[black_mask] = [0,0,255]

            

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # type: ignore
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(img_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(out_rgb)
axes[1].set_title('Processed Image')
axes[1].axis('off')
plt.show()