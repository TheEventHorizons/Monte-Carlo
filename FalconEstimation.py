import cv2
import numpy as np
import random
import os
print("Current Working Directory:", os.getcwd())

# Load the image and convert it to grayscale
img = cv2.imread("/Users/jordanmoles/falcon2.png", cv2.IMREAD_GRAYSCALE)

# Apply thresholding to obtain a binary image
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Invert the colors so that black becomes white and vice versa
thresh = cv2.bitwise_not(thresh)

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a black image to draw contours on
contour_img = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

# Draw the contours in white on the black image
cv2.drawContours(contour_img, contours, -1, (255, 255, 255), 2)

# Get the size of the image in pixels
height, width = img.shape[:2]

# Retrieve the size of the image in pixels
size = img.shape[:2]

# Set the actual dimensions of the Millennium Falcon
actual_length = 35  # in meters
actual_width = 25   # in meters

# Set the image resolution in pixels/meter
resolution = 144

# Calculate the total number of pixels in the surface of the spacecraft
total_surface_pixels = int(actual_length * actual_width * resolution**2)

# Number of random points to generate for the estimation
n = 1000000

# Number of points inside the black figure
num_points_inside = 0

# Generate random points in the image and count the number of points inside the black figure
for i in range(n):
    # Generate a random point in the image
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)

    # Check if the point is inside the black figure
    if cv2.pointPolygonTest(contours[0], (x, y), False) == 1:
        num_points_inside += 1
        # Draw the point in blue
        cv2.circle(contour_img, (x, y), 1, (255, 0, 0), -1)
    else:
        # Draw the point in red
        cv2.circle(contour_img, (x, y), 1, (0, 0, 255), -1)

# Estimate the area of the black figure using the Monte Carlo method
estimated_area = (num_points_inside / n) * (width * height)

# Estimate the area of the black figure using the Monte Carlo method
estimated_area = (num_points_inside / n) * (35 * 25)

# Display the image with points in blue and red
cv2.imshow('Image with points', contour_img)

# Wait for the user to press a key to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the estimated area of the black figure
print("Estimated area of the black figure:", estimated_area)
