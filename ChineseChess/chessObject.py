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
        self.pos_x = x_pos
        self.pos_y = y_pos
        self.is_alive = True

    def get_can_move_pos(self, board, move_area=None):
        if self.is_alive:
            return move_area
        else:
            return []

    def move(self, board, next_x, next_y):
        if [next_x, next_y] not in self.get_can_move_pos(board):
            return False
        else:
            if board[next_x][next_y] is not None:
                board[next_x][next_y].is_alive = False
            board[next_x][next_y] = board[self.pos_x][self.pos_y]
            board[self.pos_x][self.pos_y] = None
            self.pos_x = next_x
            self.pos_y = next_y
            return True

    def is_can_move(self, board, pos_x, pos_y, move_area):
        if (board[pos_x][pos_y] is None) or (board[pos_x][pos_y].color is not self.color):
            move_area.append([pos_x, pos_y])

    def get_pos(self):
        return [self.pos_x, self.pos_y]


class Soldiers(AbsChess):

    def __init__(self, chess_color, x):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        super().__init__(chess_color, x, self.y_range[3])

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for i in [[1, 0], [0, 1], [-1, 0]]:
            if (self.pos_y + i[1] in self.y_range[-5:] and self.pos_x + i[0] in X_RANGE) or (self.pos_y in self.y_range[:5] and i[0] is 0):
                self.is_can_move(board, self.pos_x + i[0], self.pos_y + i[1], move_area)

        return super().get_can_move_pos(board, move_area=move_area)


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

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            pos_x = self.pos_x + i[0]
            pos_y = self.pos_y + i[1]
            no_chess = True
            while pos_x in X_RANGE and pos_y in self.y_range:
                if board[pos_x][pos_y] is None and no_chess:
                    move_area.append([pos_x, pos_y])
                elif not no_chess:
                    if board[pos_x][pos_y] is None:
                        pos_x += i[0]
                        pos_y += i[1]
                        continue
                    elif board[pos_x][pos_y].color is not self.color:
                        move_area.append([pos_x, pos_y])
                    break
                else:
                    no_chess = False
                pos_x += i[0]
                pos_y += i[1]

        return super().get_can_move_pos(board, move_area=move_area)


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

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            pos_x = self.pos_x + i[0]
            pos_y = self.pos_y + i[1]
            while pos_x in X_RANGE and pos_y in self.y_range:
                if board[pos_x][pos_y] is None:
                    move_area.append([pos_x, pos_y])
                    pos_x += i[0]
                    pos_y += i[1]
                elif board[pos_x][pos_y].color is not self.color:
                    move_area.append([pos_x, pos_y])
                    break
                else:
                    break

        return super().get_can_move_pos(board, move_area=move_area)


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

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for way in [
            [1, 2, 0, 1],
            [-1, 2, 0, 1],
            [1, -2, 0, -1],
            [-1, -2, 0, -1],
            [2, 1, 1, 0],
            [2, -1, 1, 0],
            [-2, 1, -1, 0],
            [-2, -1, -1, 0]]:
            x = self.pos_x + way[0]
            y = self.pos_y + way[1]
            if x in X_RANGE and y in self.y_range and board[self.pos_x + way[2]][self.pos_y + way[3]] is None:
                self.is_can_move(board, x, y, move_area)

        return super().get_can_move_pos(board, move_area=move_area)


class Elephants(AbsChess):

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

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for i in [[2, 2, 1, 1], [2, -2, 1, -1], [-2, 2, -1, 1], [-2, -2, -1, -1]]:
            x = self.pos_x + i[0]
            y = self.pos_y + i[1]
            if x in X_RANGE and y in self.y_range[:5] and board[self.pos_x + i[2]][self.pos_y + i[3]] is None:
                self.is_can_move(board, x, y, move_area)

        return super().get_can_move_pos(board, move_area=move_area)


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

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for i in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            if self.pos_x + i[0] in [3, 4, 5] and self.pos_y + i[1] in self.y_range[:3]:
                self.is_can_move(board, self.pos_x + i[0], self.pos_y + i[1], move_area)

        return super().get_can_move_pos(board, move_area=move_area)


class Generals(AbsChess):

    def __init__(self, chess_color):
        if chess_color is RED:
            self.y_range = RED_COLOR_Y_RANGE
        elif chess_color is BLACK:
            self.y_range = BLACK_COLOR_Y_RANGE
        else:
            return

        super().__init__(chess_color, 4, self.y_range[0])

    def get_can_move_pos(self, board, move_area=None):
        move_area = []

        for i in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
            if self.pos_x + i[0] in [3, 4, 5] and self.pos_y + i[1] in self.y_range[:3]:
                self.is_can_move(board, self.pos_x + i[0], self.pos_y + i[1], move_area)

        return super().get_can_move_pos(board, move_area=move_area)


def __init__(self):
    return