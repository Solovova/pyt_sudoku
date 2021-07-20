import copy
import logging

from numpy import array


class DatSudokuImageClean2:
    @staticmethod
    def get_middle_black_point(img: array) -> (int, int):
        rx: int = -1
        ry: int = -1
        wy: int = len(img)
        wx: int = len(img[0])
        mid_x: int = wx // 2
        mid_y: int = wy // 2
        min_xy: int = wx + wy
        for x in range(wx):
            for y in range(wx):
                if img[y][x] != 255:
                    t_min_xy = abs(x - mid_x) + abs(y - mid_y)
                    if t_min_xy < min_xy:
                        min_xy, rx, ry = t_min_xy, x, y
        return rx, ry

    @staticmethod
    def is_near(img: array, x: int, y: int) -> bool:
        if img[y][x] == 255:
            return False
        # logging.debug(f'x,y: ({x},{y}   {img[y][x]})')
        for dx in range(-1, 2):
            for dy in range(-1, 2):

                if dx == 0 and dy == 0:
                    continue
                # logging.debug(f'dx,dy: ({x + dx},{y + dy}   {img[y + dy][x + dx]})')
                if img[y + dy][x + dx] == 254:
                    return True
        # logging.debug(f'dx,dy: __________________________________')
        return False

    @staticmethod
    def clean(img: array):
        wy = len(img)
        wx = len(img[0])
        col_gradient: int = 200

        for x in range(wx):
            for y in range(wy):
                if img[y][x] > col_gradient:
                    img[y][x] = 255

        mx, my = DatSudokuImageClean2.get_middle_black_point(img)
        # logging.debug(f'middle point: ({mx},{my})')
        img_cop = copy.deepcopy(img)
        if mx in range(wx // 3, wx // 3 * 2) and my in range(wy // 3, wy // 3 * 2):
            # logging.debug(f'middle point in range: ({mx},{my})')
            img_cop[my][mx] = 254

            while True:
                counter: int = 0
                for x in range(1, wx - 1):
                    for y in range(1, wy - 1):
                        if img_cop[y][x] != 254 and DatSudokuImageClean2.is_near(img_cop, x, y):
                            img_cop[y][x] = 254
                            counter = counter + 1
                # logging.debug(f'counter: ({counter})')
                if counter == 0:
                    break

        for x in range(wx):
            for y in range(wy):
                if img_cop[y][x] != 254:
                    img[y][x] = 255
        return img
