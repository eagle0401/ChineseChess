RED = "r"
RED_COLOR_Y_RANGE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
BLACK = "b"
BLACK_COLOR_Y_RANGE = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
X_RANGE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
R = "r"
L = "l"


class AbsChess:

    def __init__(self, chess_color, x_pos, y_pos):
        self.color = chess_color
        self._x = x_pos
        self._y = y_pos

    def get_can_move_pos(self, board):
        # return can move next position.
        return

    def move(self, board, next_x, next_y):
        if [next_x, next_y] not in self.get_can_move_pos(board):
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


class Soldiers(AbsChess):

    def __init__(self, chess_color, x):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        super().__init__(chess_color, x, self.y_range[3])

    def get_can_move_pos(self, board):
        move_area = []

        if self._y < self.y_range[5]:
            self.is_can_move(board, self._x, self._y + 1, move_area)
        elif self._y + 1 in self.y_range:
            self.is_can_move(board, self._x, self._y + 1, move_area)
        elif self._x + 1 in X_RANGE:
            self.is_can_move(board, self._x + 1, self._y, move_area)
        elif self._x - 1 in X_RANGE:
            self.is_can_move(board, self._x - 1, self._y, move_area)

        return move_area


class Cannons(AbsChess):

    def __init__(self, chess_color, side):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        if side is R:
            super().__init__(chess_color, 7, self.y_range[2])
        elif side is L:
            super().__init__(chess_color, 1, self.y_range[2])

    def get_can_move_pos(self, board):
        move_area = []

        no_chess = True
        pos_x_p = self._x + 1
        while pos_x_p in X_RANGE:
            if board[pos_x_p][self._y] is None and no_chess:
                move_area.append([pos_x_p, self._y])
            elif not no_chess:
                if board[pos_x_p][self._y] is None:
                    pos_x_p += 1
                    continue
                elif board[pos_x_p][self._y].color is not self.color:
                    move_area.append([pos_x_p, self._y])
                break
            else:
                no_chess = False
            pos_x_p += 1

        no_chess = True
        pos_x_n = self._x - 1
        while pos_x_n in X_RANGE:
            if board[pos_x_n][self._y] is None and no_chess:
                move_area.append([pos_x_n, self._y])
            elif not no_chess:
                if board[pos_x_n][self._y] is None:
                    pos_x_n -= 1
                    continue
                elif board[pos_x_n][self._y].color is not self.color:
                    move_area.append([pos_x_n, self._y])
                break
            else:
                no_chess = False
            pos_x_n -= 1

        no_chess = True
        pos_y_p = self._y + 1
        while pos_y_p in self.y_range:
            if board[self._x][pos_y_p] is None and no_chess:
                move_area.append([self._x, pos_y_p])
            elif not no_chess:
                if board[self._x][pos_y_p] is None:
                    pos_y_p += 1
                    continue
                elif board[self._x][pos_y_p].color is not self.color:
                    move_area.append([self._x, pos_y_p])
                break
            else:
                no_chess = False
            pos_y_p += 1

        no_chess = True
        pos_y_n = self._y - 1
        while pos_y_n in self.y_range:
            if board[self._x][pos_y_n] is None and no_chess:
                move_area.append([self._x, pos_y_n])
            elif not no_chess:
                if board[self._x][pos_y_n] is None:
                    pos_y_n -= 1
                    continue
                elif board[self._x][pos_y_n].color is not self.color:
                    move_area.append([self._x, pos_y_n])
                break
            else:
                no_chess = False
            pos_y_n -= 1

        return move_area


class Chariots(AbsChess):

    def __init__(self, chess_color, side):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        if side is R:
            super().__init__(chess_color, 8, self.y_range[0])
        elif side is L:
            super().__init__(chess_color, 0, self.y_range[0])

    def get_can_move_pos(self, board):
        move_area = []

        pos_x_p = self._x + 1
        while pos_x_p in X_RANGE:
            if board[pos_x_p][self._y] is None:
                move_area.append([pos_x_p, self._y])
                pos_x_p += 1
            elif board[pos_x_p][self._y].color is not self.color:
                move_area.append([pos_x_p, self._y])
                break
            else:
                break
        pos_x_n = self._x - 1
        while pos_x_n in X_RANGE:
            if board[pos_x_n][self._y] is None:
                move_area.append([pos_x_n, self._y])
                pos_x_n -= 1
            elif board[pos_x_n][self._y].color is not self.color:
                move_area.append([pos_x_n, self._y])
                break
            else:
                break
        pos_y_p = self._y + 1
        while pos_y_p in self.y_range:
            if board[self._x][pos_y_p] is None:
                move_area.append([self._x, pos_y_p])
                pos_y_p += 1
            elif board[self._x][pos_y_p].color is not self.color:
                move_area.append([self._x, pos_y_p])
                break
            else:
                break
        pos_y_n = self._y - 1
        while pos_y_n in self.y_range:
            if board[self._x][pos_y_n] is None:
                move_area.append([self._x, pos_y_n])
                pos_y_n -= 1
            elif board[self._x][pos_y_n].color is not self.color:
                move_area.append([self._x, pos_y_n])
                break
            else:
                break

        return move_area


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

        if self._x - 2 in X_RANGE and board[self._x - 1][self._y] is None:
            if self._y - 1 in self.y_range:
                self.is_can_move(board, self._x - 2, self._y - 1, move_area)
            if self._y + 1 in self.y_range:
                self.is_can_move(board, self._x - 2, self._y + 1, move_area)
        if self._x + 2 in X_RANGE and board[self._x + 1][self._y] is None:
            if self._y - 1 in self.y_range:
                self.is_can_move(board, self._x + 2, self._y - 1, move_area)
            if self._y + 1 in self.y_range:
                self.is_can_move(board, self._x + 2, self._y + 1, move_area)
        if self._y - 2 in self.y_range and board[self._x][self._y - 1] is None:
            if self._x - 1 in X_RANGE:
                self.is_can_move(board, self._x - 1, self._y - 2, move_area)
            if self._x + 1 in X_RANGE:
                self.is_can_move(board, self._x + 1, self._y - 2, move_area)
        if self._y + 2 in self.y_range and board[self._x][self._y + 1] is None:
            if self._x - 1 in X_RANGE:
                self.is_can_move(board, self._x - 1, self._y + 2, move_area)
            if self._x + 1 in X_RANGE:
                self.is_can_move(board, self._x + 1, self._y + 2, move_area)

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