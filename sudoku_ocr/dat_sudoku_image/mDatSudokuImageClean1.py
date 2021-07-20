import copy

import cv2
from numpy import array
import numpy as np


class DatSudokuImageClean1:
    @staticmethod
    def clean(img: array):
        wy = len(img)
        wx = len(img[0])
        border: int = wy // 10
        col_gradient: int = 200

        print(f'dd {wx}_{wy}')

        for x in range(wx):
            for y in range(wx):
                print(f'dd {x}_{y}')
                if img[y][x] > col_gradient:
                    img[y][x] = 255

        for x in range(border):
            count: int = 0
            for y in range(border):
                if img[y][x] <= col_gradient:
                    count = count + 1
            if count >= 1:
                for y in range(border + 1, wy - border):
                    img[y][x] = 255

        for x in range(wx - border, wx):
            count: int = 0
            for y in range(wy - border, wy):
                if img[y][x] <= col_gradient:
                    count = count + 1
            if count >= 1:
                for y in range(border + 1, wy - border):
                    img[y][x] = 255

        for y in range(border):
            count: int = 0
            for x in range(border):
                if img[y][x] <= col_gradient:
                    count = count + 1
            if count >= 1:
                for x in range(border + 1, wx - border):
                    img[y][x] = 255

        for y in range(wy - border, wy):
            count: int = 0
            for x in range(wx - border, wx):
                if img[y][x] <= col_gradient:
                    count = count + 1
            if count >= 1:
                for x in range(border + 1, wx - border):
                    img[y][x] = 255

        for x in range(border + 1):
            for y in range(border + 1):
                img[y][x] = 255

        for x in range(wx - border - 1, wx):
            for y in range(border + 1):
                img[y][x] = 255

        for x in range(border + 1):
            for y in range(wy - border - 1, wy):
                img[y][x] = 255

        for x in range(wx - border - 1, wx):
            for y in range(wy - border - 1, wy):
                img[y][x] = 255
