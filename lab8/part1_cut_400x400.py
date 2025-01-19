import cv2


def cut_the_square():
    image = cv2.imread('part1_pics/variant-8.jpg')

    height, width = image.shape[:2]
    center_x, center_y = width // 2, height // 2

    x_0 = center_x - 200
    y_0 = center_y - 200

    cutted_image = image[y_0:y_0 + 400, x_0:x_0 + 400]

    cv2.imwrite('part1_pics/variant-8_cutted.jpg', cutted_image)