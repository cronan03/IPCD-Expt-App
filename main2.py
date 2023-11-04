import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/ronan/Desktop/IPCD Project/img1.jpg')

num_rows, num_cols = 4, 6

# Calculate cell dimensions
cell_height = cropped_image.shape[0] // num_rows
cell_width = cropped_image.shape[1] // num_cols

# List to store average RGB values of each beaker
average_colors = []

# Iterate through each grid cell
for i in range(num_rows):
    for j in range(num_cols):
        # Extract the region of interest (ROI) for the current beaker
        roi = cropped_image[i * cell_height: (i + 1) * cell_height, j * cell_width: (j + 1) * cell_width]

        # Calculate the average RGB value of the liquid region in the current beaker
        average_color = np.mean(roi, axis=(0, 1)).astype(int)

        # Add the average RGB value to the list
        average_colors.append(average_color)

        # Print the average RGB value of the liquid in the current beaker
        print(f'Beaker at row {i+1}, column {j+1} has average RGB color: {average_color}')

# Draw rectangles around detected regions after processing all grid cells
for i in range(num_rows):
    for j in range(num_cols):
        top_left = (j * cell_width, i * cell_height)
        bottom_right = ((j + 1) * cell_width, (i + 1) * cell_height)
        cv2.rectangle(cropped_image, top_left, bottom_right, (0, 255, 0), 2)

cv2.imshow('Detected Beakers', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
