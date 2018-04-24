RED = "r"
RED_COLOR_Y_RANGE = [0, 1, 2, 3, 4]
BLACK = "b"
BLACK_COLOR_Y_RANGE = [9, 8, 7, 6, 5]
R = "r"
L = "l"


class AbsChess:

    def __init__(self, chess_color, x_pos, y_pos):
        self.color = chess_color
        self._x = x_pos
        self._y = y_pos

    def get_next_positions(self, board):
        # return can move next position.
        return

    def move(self, board, next_x, next_y):
        if [next_x, next_y] not in self.get_next_positions(board):
            return False
        else:
            self._x = next_x
            self._y = next_y
            return True

    def is_can_move(self, board, pos_x, pos_y, move_area):
        if (board[pos_x][pos_y] is None) or (board[pos_x][pos_y].color is not self.color):
            move_area.append([pos_x, pos_y])

    def get_pos(self):
        return [self._x, self._y]


class Horses(AbsChess):

    def __init__(self, chess_color, side):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        if side is R:
            super().__init__(chess_color, 7, self.y_range[0])
        elif side is L:
            super().__init__(chess_color, 1, self.y_range[0])

    def get_can_move_pos(self, board):
        move_area = []

        if self._x - 2 >= 0 and board[self._x - 1][self._y] is None:
            if self._y - 1 >= 0:
                self.is_can_move(board, self._x - 2, self._y - 1, move_area)
            if self._y + 1 <= 9:
                self.is_can_move(board, self._x - 2, self._y + 1, move_area)
        if self._x + 2 <= 8 and board[self._x + 1][self._y] is None:
            if self._y - 1 >= 0:
                self.is_can_move(board, self._x - 2, self._y - 1, move_area)
            if self._y + 1 <= 9:
                self.is_can_move(board, self._x - 2, self._y + 1, move_area)
        if self._y - 2 >= 0 and board[self._x][self._y - 1] is None:
            if self._x - 1 >= 0:
                self.is_can_move(board, self._x - 1, self._y - 2, move_area)
            if self._x + 1 <= 8:
                self.is_can_move(board, self._x + 1, self._y - 2, move_area)
        if self._y + 2 <= 9 and board[self._x][self._y + 1] is None:
            if self._x - 1 >= 0:
                self.is_can_move(board, self._x - 1, self._y - 2, move_area)
            if self._x + 1 <= 8:
                self.is_can_move(board, self._x + 1, self._y - 2, move_area)

        return move_area


class Elephants (AbsChess):

    def __init__(self, chess_color, side):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        if side is R:
            super().__init__(chess_color, 6, self.y_range[0])
        elif side is L:
            super().__init__(chess_color, 2, self.y_range[0])

    def get_can_move_pos(self, board):
        move_area = []

        if self._x is 0:
            self.is_can_move(board, 2, self.y_range[0], move_area)
            self.is_can_move(board, 2, self.y_range[4], move_area)
        elif self._x is 2:
            self.is_can_move(board, 4, self.y_range[2], move_area)
            self.is_can_move(board, 0, self.y_range[2], move_area)
        elif self._x is 4:
            self.is_can_move(board, 2, self.y_range[0], move_area)
            self.is_can_move(board, 2, self.y_range[4], move_area)
            self.is_can_move(board, 6, self.y_range[0], move_area)
            self.is_can_move(board, 6, self.y_range[4], move_area)
        elif self._x is 6:
            self.is_can_move(board, 4, self.y_range[2], move_area)
            self.is_can_move(board, 8, self.y_range[2], move_area)
        elif self._x is 8:
            self.is_can_move(board, 6, self.y_range[0], move_area)
            self.is_can_move(board, 6, self.y_range[4], move_area)

        return move_area


class Advisors(AbsChess):

    def __init__(self, chess_color, side):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        if side is R:
            super().__init__(chess_color, 5, self.y_range[0])
        elif side is L:
            super().__init__(chess_color, 3, self.y_range[0])

    def get_can_move_pos(self, board):
        move_area = []

        if self._y in [self.y_range[0], self.y_range[2]]:
            self.is_can_move(board, 4, self.y_range[1], move_area)
        else:
            self.is_can_move(board, 3, self.y_range[0], move_area)
            self.is_can_move(board, 5, self.y_range[0], move_area)
            self.is_can_move(board, 3, self.y_range[2], move_area)
            self.is_can_move(board, 5, self.y_range[2], move_area)

        return move_area


class Generals(AbsChess):

    def __init__(self, chess_color):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        super().__init__(chess_color, 4, self.y_range[0])

    def get_can_move_pos(self, board):
        move_area = []

        if self._y in [self.y_range[0], self.y_range[2]]:
            self.is_can_move(board, self._x, self.y_range[1], move_area)
        else:
            self.is_can_move(board, self._x, self.y_range[0], move_area)
            self.is_can_move(board, self._x, self.y_range[2], move_area)

        if self._x in [3, 5]:
            self.is_can_move(board, 4, self._y, move_area)
        else:
            self.is_can_move(board, 3, self._y, move_area)
            self.is_can_move(board, 5, self._y, move_area)

        return move_area


def __init__(self):
    return