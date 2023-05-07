import cv2
import os

# Set the source and destination directory paths
src_dir = '/path/to/source/directory'
dst_dir = '/path/to/destination/directory'

# Set the kernel size for the Gaussian blur
kernel_size = (55, 55)

# Loop through the files in the source directory
for filename in os.listdir(src_dir):
    # Read the image from the source directory
    img_path = os.path.join(src_dir, filename)
    img = cv2.imread(img_path)

    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(img, kernel_size, 0)

    # Save the blurred image to the destination directory
    dst_path = os.path.join(dst_dir, filename)
    cv2.imwrite(dst_path, blurred)
