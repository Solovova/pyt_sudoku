from PyQt5.QtCore import QThread

from sudoku_turns.mSudokuTurns import SudokuTurns


class SudokuTurnsTread(QThread):
    def __init__(self, sudoku_turns: SudokuTurns):
        QThread.__init__(self)
        self.sudoku_turns: SudokuTurns = sudoku_turns

    def run(self):
        for ind in range(len(self.sudoku_turns.matrix.turns)):
            print(self.sudoku_turns.matrix.turns[ind])
            self.sudoku_turns.do_turn(self.sudoku_turns.matrix.turns[ind], self.sudoku_turns.matrix)
