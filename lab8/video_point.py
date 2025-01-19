import cv2
import numpy as np


def find_the_point():
    pic = cv2.imread('part2_video/ref-point.jpg')
    cam = cv2.VideoCapture(0)

    threshold = 0.6

    while cam.isOpened():
        frame = capture_frame(cam)
        if frame is None:
            break

        best_loc, best_pic_dims = find_best_match(frame, pic, threshold)

        if best_loc:
            best_top_left = best_loc
            best_width, best_height = best_pic_dims
            center_x = best_top_left[0] + best_width // 2
            center_y = best_top_left[1] + best_height // 2

            draw_lines_from_the_center(frame, center_x, center_y)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam_stop(cam)


def find_best_match(frame, pic, threshold):
    best_match = -1
    best_loc = None
    best_pic_dims = (pic.shape[1], pic.shape[0])

    for scale in np.linspace(0.5, 1.5, 10):
        resized_pic = cv2.resize(pic, (int(pic.shape[1] * scale), int(pic.shape[0] * scale)))
        resized_h, resized_w = resized_pic.shape[:2]

        if check_for_fit(frame, resized_h, resized_w):
            continue

        result = cv2.matchTemplate(frame, resized_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold and max_val > best_match:
            best_match = max_val
            best_loc = max_loc
            best_pic_dims = (resized_w, resized_h)

    return best_loc, best_pic_dims


def check_for_fit(frame, resized_h, resized_w):
    return frame.shape[0] < resized_h or frame.shape[1] < resized_w


def draw_lines_from_the_center(frame, center_x, center_y):
    cv2.line(frame, (0, center_y), (frame.shape[1], center_y), (255, 105, 180), 2)
    cv2.line(frame, (center_x, 0), (center_x, frame.shape[0]), (255, 105, 180), 2)


def cam_stop(cam):
    cam.release()
    cv2.destroyAllWindows()


def capture_frame(cam):
    ret, frame = cam.read()
    if not ret:
        return None
    return frame
