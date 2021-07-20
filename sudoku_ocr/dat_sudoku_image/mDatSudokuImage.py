import copy
import os
from typing import Union

import cv2
import numpy as np
from PIL import Image, ImageGrab

from sudoku_ocr.dat_sudoku_image.mDatSudokuImageClean2 import DatSudokuImageClean2


class DatSudokuImage:
    def __init__(self, area: Union[list[int], None], filename: Union[str, None], width: int, height: int):
        self.width = width
        self.height = height
        if area is not None:
            self.img_grab = ImageGrab.grab(bbox=(area[0], area[1], area[2], area[3]))

        if filename is not None:
            if not os.path.isfile(filename):
                raise Exception(f'DatSudokuImage Init not file {filename}')
            self.img_grab = Image.open(filename)

        self.img_np: np.array = cv2.cvtColor(np.array(self.img_grab), cv2.COLOR_RGB2BGR)
        self.img_height: int = len(self.img_np)
        self.img_width: int = len(self.img_np[0])

        screenshot = cv2.cvtColor(self.img_np, cv2.COLOR_BGR2GRAY)
        self.img_np_bw = cv2.medianBlur(screenshot, 3)

        wx = self.img_width // self.width
        wy = self.img_height // self.height

        self.img_parts: list[list[np.array]] = [
            [copy.copy(self.img_np_bw[wy * y:wy * (y + 1), wx * x:wx * (x + 1)]) for x in range(self.width)]
            for y in range(self.height)]

        self.img_parts_clean: list[list[np.array]] = copy.deepcopy(self.img_parts)


    def show_img(self):
        cv2.namedWindow("image")
        cv2.imshow("image", self.img_np)

    def show_break_up_img(self, tx: Union[int, None] = None, ty: Union[int, None] = None):
        if tx is not None and ty is not None:
            window_name: str = f'({tx},{ty})'
            cv2.namedWindow(window_name)
            cv2.imshow(window_name, self.img_parts[ty][tx])
            return

        for x in range(self.width):
            for y in range(self.height):
                window_name: str = f'({x},{y})'
                cv2.namedWindow(window_name)
                cv2.imshow(window_name, self.img_parts[y][x])

    def show_break_up_clean_img(self, tx: Union[int, None] = None, ty: Union[int, None] = None):
        if tx is not None and ty is not None:
            window_name: str = f'clean ({tx},{ty})'
            cv2.namedWindow(window_name)
            cv2.imshow(window_name, self.img_parts_clean[ty][tx])
            return

        for x in range(self.width):
            for y in range(self.height):
                window_name: str = f'clean ({x},{y})'
                cv2.namedWindow(window_name)
                cv2.imshow(window_name, self.img_parts_clean[y][x])

    def clean_parts(self, tx: Union[int, None] = None, ty: Union[int, None] = None):
        if tx is not None and ty is not None:
            DatSudokuImageClean2.clean(self.img_parts_clean[ty][tx])
            return

        for x in range(self.width):
            for y in range(self.height):
                DatSudokuImageClean2.clean(self.img_parts_clean[y][x])
