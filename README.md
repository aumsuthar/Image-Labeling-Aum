## Image Labeling Tool with Python and OpenCV

This Python program utilizes OpenCV for image labeling and is designed for integration into larger projects. Refer to the `make_box.py` file for detailed instructions. This program uses OpenCV and Python to draw boxes over images, saves the images in the boxes after applying a smoothing filter to them, for use in computer vision and ML/AI. The images are taken from the following link: https://www.kaggle.com/datasets/aman2000jaiswal/agriculture-crop-images

**Installation:**

1. Download required libraries using pip:

   ```
   pip install cv2 
   ```
   ```
   pip install argparse
   ```
   ```
   pip install os
   ```
   ```
   pip install Pillow
   ```
   ```
   pip install numpy
   ```
   ```
   pip install pathlib
   ```
**Usage:**

1. **File Paths:**

   - Update the following lines within `make_box.py` to specify your file paths:
      - Line 50: Path to your unlabeled images folder.
      - Line 47: Path to your labeled images folder.
      - Line 37: Path to a folder for storing regions of interest (ROI) for each image.
      - Line 71: Path to the folder for deleted cropped images (same as line 37).

2. **Keyboard Controls:**

   - Use the following keys during program execution:
      - `s`: Save the current image to the labeled images folder (line 47).
      - `d`: Delete the most recently cropped image (line 37 & 71).
      - `n`: Move to the next unlabeled image (line 50).
      - `r`: Clear all drawn bounding boxes on the current image.
      - `c`: Exit the program.
      - Left-click & drag: Define regions of interest (ROI) using a bounding box.

3. **Run the Program:**

   Execute `make_box.py` to start the image labeling process.

