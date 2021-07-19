import copy
import logging
import time

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from pytesseract import pytesseract

from sudocu_solution.data.dat_matrix.mDatMatrixLoader import DatMatrixLoader
from sudocu_solution.data.dat_matrix.mDatMatrixSetState import DatMatrixSetState
from sudocu_solution.data.dat_matrix.mDatMatrixToStr import DatMatrixToStr
from sudocu_solution.data.mDatMatrix import DatMatrix
from sudocu_solution.data.mDatTurn import DatTurn
from sudocu_solution.schema.mSudSchema import SudSchema
from sudocu_solution.schema.mSudSchemaJson import SudSchemaJson
from sudocu_solution.solver.mSudokuSolver import SudokuSolver


class Ocr:
    def __init__(self, area: list[int], dimension: int, area_buttons: list[int]):
        self.area = area
        self.dimension = dimension
        self.area_buttons = area_buttons

    def get_subarea_buttons(self, area: list[int], dig: int, dimension: int) -> list[int]:
        wx: int = (area[2] - area[0]) // dimension
        sx: int = area[0] + wx * (dig - 1)
        return list([sx, area[1], sx + wx, area[3]])

    def m_click_area(self, area: list[int]):
        x = int((area[0] + area[2]) // 2)
        y = int((area[1] + area[3]) // 2)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

    def n_do_turn(self, turn: DatTurn):
        subarea = self.get_subarea(self.area, turn.x, turn.y, self.dimension)
        self.m_click_area(subarea)
        subarea_buttons = self.get_subarea_buttons(self.area_buttons, turn.digit, self.dimension)
        self.m_click_area(subarea_buttons)

    def n_solve(self, sol: DatMatrix):
        for ind in range(len(sol.turns)):
            print(sol.turns[ind])
            self.n_do_turn(sol.turns[ind])

    def n_clean_img(self, img):
        wy = len(img)
        wx = len(img[0])
        border: int = wy // 7
        col_gradient: int = 210

        for x in range(wx):
            for y in range(wy):
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

        return img

    def n_get_img(self, x: int, y: int):
        subarea = self.get_subarea(self.area, x, y, self.dimension)
        screenshot = np.array(ImageGrab.grab(bbox=(subarea[0], subarea[1], subarea[2], subarea[3])))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # pylint: disable=no-member
        screenshot = cv2.medianBlur(screenshot, 3)  # pylint: disable=no-member

        screenshot = cv2.resize(screenshot, (30, 30), interpolation=cv2.INTER_CUBIC)
        # screenshot = cv2.threshold(screenshot, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return self.n_clean_img(screenshot)

    def n_sudoku_is_number(self, arr) -> bool:
        return np.average(arr, axis=None, weights=None, returned=False) < 250

    def n_sudoku_str_to_int(self, str):
        result = ""
        for s in str:
            if s in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                result = result + s
        return result

    def n_get_digit_all(self):
        l_scr = list()
        res: list[list[int]] = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        for y in range(self.dimension):
            for x in range(self.dimension):
                scr = self.n_get_img(x, y)
                if self.n_sudoku_is_number(scr):
                    res[y][x] = -1
                    l_scr.append(scr)

        sum_scr = copy.copy(l_scr[0])
        for ind in range(1, len(l_scr)):
            sum_scr = np.concatenate((sum_scr, l_scr[ind]), axis=1)

        # scr1 = self.n_get_img(0, 0)[2:-2, 2:-2]
        # scr2 = self.n_get_img(2, 0)[2:-2, 2:-2]
        # cv2.namedWindow("name1")
        # cv2.imshow("name1", scr1)
        # cv2.namedWindow("name2")
        # cv2.imshow("name2", scr2)
        #
        # sum_scr = np.concatenate((scr1, scr2), axis=1)
        # cv2.namedWindow("name3")
        # cv2.imshow("name3", sum_scr)
        # config = "--oem 3  --psm 6 outputbase digits"
        rec_str = pytesseract.image_to_string(sum_scr, config="--oem 3  --psm 6 outputbase digits")
        test_str = "38169169257486738738941342795246631927"
        rec_str = self.n_sudoku_str_to_int(rec_str)

        for y in range(self.dimension):
            for x in range(self.dimension):
                if res[y][x] == -1:
                    res[y][x] = int(rec_str[0])
                    rec_str = rec_str[1:]

        li: list[str] = ["" for _ in range(self.dimension)]
        for y in range(self.dimension):
            for x in range(self.dimension):
                if res[y][x] == 0:
                    li[y] = li[y] + " "
                else:
                    li[y] = li[y] + str(res[y][x])
        print(li)

        try:
            schema_json: SudSchemaJson = SudSchemaJson()
            schema: SudSchema = SudSchema(schema_json)
            matrix = DatMatrixLoader.instance_matrix(schema)
            DatMatrixSetState.set_state(matrix, li)
            solver: SudokuSolver = SudokuSolver(matrix)
            if solver.solve():
                self.n_solve(solver.solutions[0])

            logging.info(f'\nSolutions: {len(solver.solutions)}')
            for ind in range(len(solver.solutions)):
                logging.info(f'\nSolution: {ind + 1}')
                logging.info(f'\n{DatMatrixToStr.matrix_to_str_digit(solver.solutions[ind])}')
        except Exception as e:
            logging.error(f'Exception {e}', exc_info=True)

        # print(rec_str)
        # print(test_str)

    def get_digit_from_x_y(self, x: int, y: int, window_name: str = "") -> str:
        subarea = self.get_subarea(self.area, x, y, self.dimension)
        dig_str = self.get_image(subarea, "name")
        logging.debug(f'({x},{y}) {subarea} "{dig_str}"')
        return dig_str

    def get_digit_all(self) -> list[list[str]]:
        sudoku_list: list[list[str]] = [["" for _ in range(self.dimension)] for _ in range(self.dimension)]

        for x in range(self.dimension):
            for y in range(self.dimension):
                dig_str = self.get_digit_from_x_y(x, y)
                sudoku_list[y][x] = dig_str
        return sudoku_list

    def to_str(self, sudoku_list: list[list[str]]) -> str:
        result: str = "\n"
        for y in range(len(sudoku_list[0])):
            line: str = ""
            for x in range(len(sudoku_list[y][0])):
                tmp_str = f'"{sudoku_list[y][x]}"'
                while len(tmp_str) < 8:
                    tmp_str = " " + tmp_str
                line = line + tmp_str
            result = result + "\n" + line
        return result

    def get_image(self, area, name_window: str = ""):
        screenshot = np.array(ImageGrab.grab(bbox=(area[0], area[1], area[2], area[3])))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # pylint: disable=no-member
        # screenshot = cv2.bitwise_not(screenshot)  # pylint: disable=no-member

        screenshot = cv2.medianBlur(screenshot, 3)  # pylint: disable=no-member

        screenshot = cv2.resize(screenshot, (30, 30), interpolation=cv2.INTER_CUBIC)
        screenshot = cv2.threshold(screenshot, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # screenshot = self.sudoku_get_without_border(screenshot, 2)

        if name_window != "":
            cv2.namedWindow(name_window)  # pylint: disable=no-member
            cv2.imshow(name_window, screenshot)  # pylint: disable=no-member

        custom_config = r'--oem 3 --psm 10 outputbase digits'
        # , timeout=0.5
        # , config=custom_config
        rec_str = pytesseract.image_to_string(screenshot, config="--oem 3  --psm 10 outputbase digits")
        return rec_str

    # ------>
    def get_sudoku(self):
        # sudoku_list = self.get_digit_all()
        # logging.debug(self.to_str(sudoku_list))
        # a_string = self.get_digit_from_x_y(8, 0, "name")
        # print([ord(elem) for elem in a_string])
        #
        # logging.debug(a_string)

        self.n_get_digit_all()
        pass

    def get_subarea(self, area: list[int], x: int, y: int, dimension: int) -> list[int]:
        wx: int = (area[2] - area[0]) // dimension
        wy: int = (area[3] - area[1]) // dimension
        sx: int = area[0] + wx * x
        sy: int = area[1] + wy * y

        return list([sx, sy, sx + wx, sy + wy])

    def sudoku_str_to_int(self, str):
        result = ""
        for s in str:
            if s in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                result = result + s
        # print("-->"+result)
        if len(result) == 0:
            return 0
        return int(result)

    def sudoku_get_without_border(self, arr, border: int):
        wy = len(arr)
        wx = len(arr[0])
        return arr[border:wx - border, border:wy - border]

    def sudoku_is_number(self, arr) -> bool:
        return np.average(arr, axis=None, weights=None, returned=False) > 5

    def get_tess_area_ocr(self, area, name_window: str = ""):
        screenshot = np.array(ImageGrab.grab(bbox=(area[0], area[1], area[2], area[3])))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # pylint: disable=no-member
        # screenshot = cv2.bitwise_not(screenshot)  # pylint: disable=no-member
        # screenshot = cv2.threshold(screenshot, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        screenshot = cv2.medianBlur(screenshot, 3)  # pylint: disable=no-member
        # screenshot = self.sudoku_get_without_border(screenshot, 2)

        if name_window != "":
            cv2.namedWindow(name_window)  # pylint: disable=no-member
            cv2.imshow(name_window, screenshot)  # pylint: disable=no-member

        custom_config = r'--oem 3 --psm 10 outputbase digits'
        # , timeout=0.5
        # , config=custom_config
        rec_str = pytesseract.image_to_string(screenshot, config="--oem 3  --psm 6 outputbase digits")
        return rec_str
