import cv2


def save_image(path, image):

    cv2.imwrite(path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))