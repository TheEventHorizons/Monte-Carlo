# Monte-Carlo README

This repository contains a Python script for estimating the area of a figure in an image using the Monte Carlo method. The figure represents the silhouette of the Millennium Falcon from Star Wars.

## Prerequisites

Ensure you have the required libraries installed:

- cv2 (OpenCV)
- numpy
- random
- os

You can install OpenCV using the following command:

```bash
pip install opencv-python
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/TheEventHorizons/Monte-Carlo.git
cd Monte-Carlo
```

2. Run the script:

```bash
python FalconEstimation.py
```

The script loads an image, applies thresholding, finds contours, generates random points, and estimates the area using the Monte Carlo method.

## Script Overview

- `FalconEstimation.py`: The main Python script.
- `README.md`: This README file providing instructions and an overview of the script.
- `ImageFalcon.png`: The image of the Millennium Falcon silhouette.

## Image and Contour Processing

The script loads the image, converts it to grayscale, applies thresholding, and finds contours. It then generates random points and counts the number of points inside the black silhouette.

## Area Estimation

The Monte Carlo method is used to estimate the area of the black silhouette based on the ratio of points inside the figure to the total number of generated points.

## Result

The script displays the image with points in blue and red, waits for user input to close the window, and prints the estimated area of the black figure.

For a detailed explanation and insights into the Monte Carlo method and its applications, visit my [scientific outreach website](https://theeventhorizons.com/stormtroopers/).

Feel free to experiment with different images or modify the script to suit your needs.

Happy coding!