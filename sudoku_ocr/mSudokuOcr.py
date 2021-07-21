import copy
import logging
from typing import Union

import cv2
import numpy as np
from pytesseract import pytesseract

from sudoku_ocr.dat_sudoku_image.mDatSudokuImage import DatSudokuImage
from sudoku_solution.data.dat_matrix.mDatMatrixLoader import DatMatrixLoader
from sudoku_solution.data.dat_matrix.mDatMatrixSetState import DatMatrixSetState
from sudoku_solution.data.mDatMatrix import DatMatrix
from sudoku_solution.schema.mSudSchema import SudSchema
from sudoku_solution.schema.mSudSchemaJson import SudSchemaJson
from sudoku_solution.solver.mSudokuSolver import SudokuSolver


class SudokuOcr:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dat_sudoku_image: Union[DatSudokuImage, None] = None

    def set_img(self, area: Union[list[int], None] = None, filename: Union[str, None] = None) -> bool:
        try:
            self.dat_sudoku_image: DatSudokuImage = DatSudokuImage(area, filename, width=self.width, height=self.height)
            return True
        except Exception as e:
            logging.warning(e)
            return False

    def is_number(self, img) -> bool:
        return np.average(img, axis=None, weights=None, returned=False) < 250

    def sudoku_str_to_int(self, in_str: str):
        result = ""
        for s in in_str:
            if s in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                result = result + s
        return result

    def get_list(self):
        l_scr = list()
        res: list[list[int]] = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                img = self.dat_sudoku_image.img_parts_clean[y][x]
                if self.is_number(img):
                    res[y][x] = -1
                    l_scr.append(img)

        sum_scr = copy.copy(l_scr[0])
        for ind in range(1, len(l_scr)):
            sum_scr = np.concatenate((sum_scr, l_scr[ind]), axis=1)

        sum_scr = cv2.resize(sum_scr, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

        l_add: np.array = np.array([[255 for _ in range(len(sum_scr[0]))] for _ in range(3)])
        l_add = l_add.astype(np.uint8)
        sum_scr = copy.copy(np.append(sum_scr, l_add, axis=0))

        if logging.DEBUG <= logging.root.level:
            cv2.namedWindow("sum_scr")
            cv2.imshow("sum_scr", sum_scr)

        rec_str = pytesseract.image_to_string(sum_scr, config="--oem 3  --psm 6 outputbase digits")
        logging.info(f'ocr_real: ({rec_str})')
        rec_str = self.sudoku_str_to_int(rec_str)
        logging.info(f'ocr_corr: ({rec_str})')

        for y in range(self.height):
            for x in range(self.width):
                if res[y][x] == -1:
                    res[y][x] = int(rec_str[0])
                    rec_str = rec_str[1:]

        li: list[str] = ["" for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if res[y][x] == 0:
                    li[y] = li[y] + " "
                else:
                    li[y] = li[y] + str(res[y][x])
        logging.debug(f'list: ({li})')
        return li
