import numpy as np
import matplotlib.pyplot as plt
import cv2


def convolve(image, kernel):
    
    if kernel.shape[0] != kernel.shape[1] :
        print("Kernel must be square")
        return None
    elif kernel.shape[0] % 2 == 0 :
        print("Kernel size must be odd")
        return None
    else :
        new_kernel = np.flipud(np.fliplr(kernel))

        height , width = image.shape 
        pad_value = new_kernel.shape[0] // 2
        kernel_size = new_kernel.shape[0]


        padded_image = np.pad(image , pad_value , mode = 'constant' , constant_values= 0)

        new_image = np.zeros_like(image,dtype= np.float32)
        
        
        for i in range(height):
            for j in range(width):
                areatobe_dotted = padded_image[i:i + kernel_size, j : j + kernel_size]
                val = np.sum(areatobe_dotted * new_kernel)
                new_image[i,j] = val
        return np.clip(new_image , 0 , 255)
    
def median_kernel(image , kernel_size):
    height , width = image.shape 
    pad_value = kernel_size // 2
    padded_image = np.pad(image , pad_value , mode = 'constant' , constant_values= 0)
    new_image = np.zeros_like(image,dtype= np.float32)
    
    
    for i in range(height):
        for j in range(width):
            areatobe_dotted = padded_image[i:i + kernel_size, j : j + kernel_size]
            val = np.median(areatobe_dotted)
            new_image[i,j] = val
    return np.clip(new_image , 0 , 255)
        
    
        


# Take notice that OpenCV handles the image as a numpy array when opening it
img = cv2.imread(r'C:\Users\Lenovo\OneDrive\Desktop\AUR-Training-25\phase 2\AUR-Training-25\AUR-Training-25\Phase_2\Session 3\image.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found.")
    exit()

fig, axes = plt.subplots(2, 3, figsize=(8, 8))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25), cmap='gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')

axes[1, 0].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])), cmap='gray')
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(convolve(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])), cmap='gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')

axes[0, 2].imshow(convolve(img, np.array([ [0.0625, 0.125, 0.0625],[0.125,  0.25,  0.125 ],[0.0625, 0.125, 0.0625] ])), cmap='gray')
axes[0, 2].set_title('Gaussian Filter')
axes[0, 2].axis('off')

axes[1, 2].imshow(median_kernel(img , 3), cmap='gray')
axes[1, 2].set_title('Median Filter')
axes[1, 2].axis('off')


plt.show()


