import cv2
import numpy as np


def show_only_blue_color(original_img):

    # Read the image
    image = cv2.imread(original_img)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper boundaries of the blue color in HSV
    lower_blue = np.array([100, 50, 50])  # Lower blue threshold (adjust values if needed)
    upper_blue = np.array([130, 255, 255])  # Upper blue threshold (adjust values if needed)

    # Create a binary mask for the blue color range
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Apply the mask to the original image to extract blue colors
    blue_image = cv2.bitwise_and(image, image, mask=blue_mask)

    # Show the blue image
    cv2.imshow('Blue Image', blue_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_bounding_box(image, object_name):

    # Draw a bounding box around the object
    # (x, y) is the top-left corner and (w, h) is the width and height of the box
    x, y, w, h = 20, 25, 235, 180
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Write the object name next to the bounding box
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_thickness = 2
    text_size = cv2.getTextSize(object_name, font, font_scale, font_thickness)[0]
    text_x = x + int((w - text_size[0]) / 2)
    text_y = y + w
    cv2.putText(image, object_name, (text_y, text_x), font, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)

    # Saving the image with the bounding box and object name
    cv2.imwrite('output_image.jpg', image)

    # Displaying the image with the bounding box and object name
    cv2.imshow('Image with Bounding Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    img_path = 'Images/cargo_live_animals_parrot.jpg'
    object_name = "parrot"

    # Read the image
    img = cv2.imread(img_path)

    # Displaying the original image
    cv2.imshow('Original image', img)
    cv2.waitKey(0)

    # Show only blue color
    show_only_blue_color(img_path)

    # Draw bounding box on the original image
    draw_bounding_box(img, object_name)
