# Image Processing Tools

## Description
Image Processing Tools is a Python-based application that provides a graphical user interface (GUI) for performing various image processing operations. It includes functions for Fourier transformations, filtering, ROI analysis, and morphological operations like erosion and dilation. Additionally, it offers a range of features for image enhancement, restoration, segmentation, measurements, registration, compression, and visualization.

## Features

### Image Enhancement:
- Histogram equalization for improving contrast and distribution of pixel intensities.
- Adaptive histogram equalization for enhancing local contrast in different regions.
- Gamma correction for adjusting overall brightness and contrast.

### Image Restoration:
- Noise reduction using filters such as median filter, Gaussian filter, and bilateral filter.
- Image deblurring to recover sharpness and reduce blurriness caused by motion or defocus.

### Image Segmentation:
- Thresholding techniques for separating objects from the background based on pixel intensity.
- Edge detection algorithms like Canny, Sobel, and Laplacian for detecting and extracting edges.
- Clustering algorithms such as K-means and watershed for grouping pixels into meaningful regions.

### Image Measurements:
- Calculation of image properties such as area, perimeter, centroid, and bounding box.
- Object counting and labeling for quantifying the number of distinct objects in an image.
- Shape analysis to extract features like circularity, elongation, and aspect ratio.

### Image Registration:
- Alignment of multiple images to compensate for geometric or spatial differences.
- Transformation functions like translation, rotation, scaling, and affine transformations.

### Image Compression:
- Lossless compression techniques such as Huffman coding and Run-Length Encoding (RLE).
- Lossy compression techniques like Discrete Cosine Transform (DCT) and JPEG compression.

### Image Visualization:
- Image display with zooming and panning capabilities.
- Image annotation with text, arrows, and shapes for highlighting specific regions.

## Usage
To use the image processing tools, follow these steps:

1. Install the required dependencies mentioned in the "Installation" section.
2. Run the main application script (`main.py`) using a Python interpreter.
3. The GUI will be displayed, providing various options for image processing.
4. Load an image from your local system or capture one using a connected camera.
5. Choose the desired image processing operation from the available tools.
6. Adjust the parameters or select the region of interest (if applicable).
7. Apply the chosen operation and view the resulting image.
8. Save the processed image if desired.

## Installation
To install and set up the image processing tools, follow these steps:

1. Clone the project repository from the GitHub URL: `https://github.com/your-username/image-processing-tools.git`.
2. Navigate to the project directory on your local system.
3. Create a virtual environment (optional but recommended) using `python -m venv env`.
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install the required dependencies by running `pip install -r requirements.txt`.

## Contributing
Contributions to this image processing tool project are welcome. If you
