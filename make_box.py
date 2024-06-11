# import the necessary packages
import cv2
import argparse
import os

# now let's initialize the list of reference point
ref_point = []
text_point = []
all_boxes = []
file_index_cropped = 0

def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point, crop, text_point, all_boxes, file_index_cropped
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        text_point = [(x, y-6)] # this is the position of the text label above the box
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))
        text_point.append((x, y))
        font = cv2.FONT_HERSHEY_DUPLEX
        fontscale = 0.35
        thickness = 1
        color = (0, 0, 255) #red
        x1, y1 = ref_point[0]
        x2, y2 = ref_point[1]
        # draw a rectangle around the region of interest
        cv2.rectangle(image, ref_point[0], ref_point[1], color, 2)
        os.chdir('C:\\Users\\suthaa2\\Downloads\\imagec_ui\\labelled_images\\cropped_images')
        cropped_img = cv2.getRectSubPix(image, (x2-x1, y2-y1), (x1+((x2-x1)/2), y1+((y2-y1)/2)))
        cv2.imwrite(f"cropped_image_{file_index_cropped}.png", cropped_img)
        cv2.putText(image,"plant", text_point[0], font, fontscale, color, thickness, cv2.LINE_AA, False)
        cv2.imshow("image", image)
        file_index_cropped += 1
 
directory_labelled = 'C:\\Users\\suthaa2\\Downloads\\imagec_ui\\labelled_images'
file_index = 0
ul_file_index = 0
image_dir = 'C:\\Users\\suthaa2\\Downloads\\imagec_ui\\crop_images\\sugarcane'
image_list = os.listdir(image_dir)

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(os.path.join(image_dir, image_list[ul_file_index]))
img = image
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # press 'r' to reset the window
    if key == ord("s"):
        os.chdir(directory_labelled)
        cv2.imwrite(f"labelled_img_{file_index}.png",img)
        file_index += 1
        print('Image saved.')
        print(os.listdir(directory_labelled))
    if key == ord("n"):
        ul_file_index += 1
        image = clone.copy()
        image_path = os.path.join(image_dir, image_list[ul_file_index])
        image = cv2.imread(image_path)
        img = image
    if key == ord("r"):
        image = clone.copy()
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
# close all open windows
cv2.destroyAllWindows() 