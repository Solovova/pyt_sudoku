import time

import cv2
import numpy as np
from PIL import ImageGrab


class CvDev:
    @staticmethod
    def test1(image):
        result = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 9)

        # Fill rectangular contours
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(thresh, [c], -1, (255, 255, 255), -1)

        # Morph open
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=10)

        # Draw rectangles
        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 3)

        cv2.imshow('thresh', thresh)
        cv2.imshow('opening', opening)
        cv2.imshow('image', image)
        cv2.waitKey()

    @staticmethod
    def find_rect(area: list[int]):
        img_grab = ImageGrab.grab(bbox=(0, 0, 1919, 1079))  # x, y, w, h
        img_grab = cv2.cvtColor(np.array(img_grab), cv2.COLOR_RGB2BGR)
        CvDev.test1(img_grab)
        # gray = cv2.cvtColor(img_grab, cv2.COLOR_BGR2GRAY)
        #
        # binary = cv2.bitwise_not(gray)
        #
        # contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST,
        #                                        cv2.CHAIN_APPROX_SIMPLE)
        #
        # for contour, hier in zip(contours, hierarchy):
        #     (x, y, w, h) = cv2.boundingRect(contour)
        #     cv2.rectangle(img_grab, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #
        # cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
        #
        # cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        #
        # while True:
        #     cv2.imshow("image", img_grab)
        #     time.sleep(0.1)
        #     key = cv2.waitKey(1)
        #     if key == 27:
        #         cv2.destroyAllWindows()
        #         return
