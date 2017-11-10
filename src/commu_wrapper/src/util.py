import random
import time

import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

# Necessary to transform ROS images into OpenCv images for caffe
bridge = CvBridge()


def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return retval

    return wrapper


def draw_bounding_boxes(cv_image, classification_results):
    # type: (np.array, ssd.msg.ClassifiedObjectArray) -> (np.array)
    """
    Draws classification bounding boxes on image
    :param cv_image: The image in opencv format.
    :param classification_results: The results from classifying this image
    :return: The image, with bounding boxes and labels explaining the classification.
    """

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    font_scale = 1
    font_thickness = 1
    text_margin = 5

    for result in classification_results:
        top_left = np.array((int(result.bbox.x_min), int(result.bbox.y_min)))
        bottom_right = np.array(
            (int(result.bbox.x_min + result.bbox.x_size), int(result.bbox.y_min + result.bbox.y_size)))

        text = '{:.2f}: {}'.format(result.score, result.label)

        color = random_color()

        cv2.rectangle(cv_image, (top_left[0], top_left[1]), (bottom_right[0], bottom_right[1]), color, thickness=1)

        text_width, text_height = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

        text_bottom_left = top_left + np.array((text_margin, -text_margin))
        text_top_right = text_bottom_left + np.array((text_width, -text_height))

        cv2.rectangle(cv_image, (text_bottom_left[0] - text_margin, text_bottom_left[1] + text_margin),
                      (text_top_right[0] + text_margin * 2, text_top_right[1] - text_margin * 2),
                      (color[0], color[1], color[2]), thickness=cv2.FILLED)

        cv2.putText(cv_image, text, (text_bottom_left[0], text_bottom_left[1]), font, font_scale, (0, 0, 0, 255),
                    thickness=font_thickness)
    return cv_image


def draw_crosshair(cv_image, x, y, width=6, height=6, line_thickness=3):
    # type: (np.array, int, int) -> np.array
    """
    Draw crosshair on cv image.
    :param cv_image: The image to draw the crosshair on.
    :param x: The x coordinate of the center of the crosshair
    :param y: The y coordinate of the center of the crosshair
    :return: The cv_image with the crosshair drawn.
    """

    l1x1 = int(x - (width / 2))
    l1y1 = y
    l1x2 = int(x + (width / 2))
    l1y2 = y

    l2x1 = x
    l2y1 = int(y - (height / 2))
    l2x2 = x
    l2y2 = int(y + (height / 2))

    cv2.line(cv_image, (l1x1, l1y1), (l1x2, l1y2), random_color(), line_thickness)
    cv2.line(cv_image, (l2x1, l2y1), (l2x2, l2y2), random_color(), line_thickness)

    return cv_image


def draw_text(cv_image, text, x, y, font=cv2.FONT_HERSHEY_COMPLEX_SMALL, font_scale=1, color=(0, 0, 0),
              font_thickness=1, background=False, background_color=(1, 1, 1), text_margin=5):
    # type: (np.array, str, int, int, int, int, (int, int, int), int, bool, (int, int, int), int) -> np.array
    """
    Draw text on the provided cv2 image at a specified position
    :param cv_image: The image to draw the text on.
    :param text: The text to draw
    :param x: The x coordinate of the top-left corner of the text.
    :param y: The y coordinate of the top-left corner of the text.
    :param font: The font to draw in.
    :param font_scale: The size of the font.
    :param color: The color of the text.
    :param font_thickness: The thickness of the font.
    :param background: Whether to add a rectangular colored background to the text to provide contrast.
    :param background_color: The color this background should be.
    :param text_margin: The margin between the edge of the background and the text.
    :return: The cv image with the specified text.
    """

    text_width, text_height = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    text_bottom_left = (x, y) + np.array((text_margin, -text_margin))
    text_top_right = text_bottom_left + np.array((text_width, -text_height))

    if background:
        cv2.rectangle(cv_image, (text_bottom_left[0] - text_margin, text_bottom_left[1] + text_margin),
                      (text_top_right[0] + text_margin * 2, text_top_right[1] - text_margin * 2),
                      background_color, thickness=cv2.FILLED)

    cv2.putText(cv_image, text, (text_bottom_left[0], text_bottom_left[1]), font, font_scale, color,
                thickness=font_thickness)

    return cv_image


def image_to_opencv(image_data):
    try:
        return bridge.imgmsg_to_cv2(image_data, "bgr8")
    except CvBridgeError as e:
        print(e)

def random_color():
    return random.sample(xrange(0, 255), 3)


def approximate_say_time(utterance):
    """
    Approximates the time it takes for the CommU to utter a string of text in seconds. Only tested on English.
    :param utterance: The utterance to approximate pronunciation time for.
    :return: The approximate time it will take for the CommU to pronounce the specified utterance.
    """
    return len(utterance) * (1.0 / 6.5) / 3.0 + 1.5


def add_alpha_layer(cv_image, value = 255):
    # type: (np.array) -> np.array
    """
    Adds an alpha layer to an bgr cv image.
    :param cv_image: The BGR image to add an alpha layer to.
    :param value: The value to initialize the alpha layer with.
    :return: The same image, with an alpha layer.
    """

    b, g, r = cv2.split(cv_image)
    alpha = np.full(b.shape, value, dtype=b.dtype)

    merged = cv2.merge((b, g, r, alpha))

    print merged.shape

    return merged


def draw_image_margin(cv_image, margin_size=50):
    # type: (np.array, int, (int, int, int)) -> np.array
    """
    Draw a margin around an image of the specified color and size.
    :param cv_image: The image to draw a margin around.
    :param margin_size: The size of the margin.
    :param margin_color: The color of the margin.
    :return: The image with a margin.
    """
    shape = cv_image.shape
    new_shape = (shape[0] + margin_size * 2, shape[1] + margin_size * 2, shape[2])

    new_image = np.full(new_shape, 255, cv_image.dtype)
    new_image[margin_size:margin_size + shape[0], margin_size:margin_size + shape[1]] = cv_image

    return new_image


def draw_overlay_image(base_cv_image, overlay_cv_image):
    # type: (np.array, np.array) -> np.array
    """
    Overlays an image with an alpha channel over a base. Both images should have an alpha channel
    :param base_cv_image: The image to draw the overlay on top of. All alpha data of this image gets discarded.
    :param overlay_cv_image: The image to overlay on top of the base image.
    :return: The cv image resulting from the merge.
    """

    # Split out the transparency mask from the colour info
    overlay_img = overlay_cv_image[:, :, :3] # Grab the BRG planes
    overlay_mask = overlay_cv_image[:, :, 3:]  # And the alpha plane

    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask

    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out base image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    base_part = (base_cv_image * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image
    return np.uint8(cv2.addWeighted(base_part, 255.0, overlay_part, 255.0, 0.0))

