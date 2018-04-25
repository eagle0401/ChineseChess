import ChineseChess.chessObject as cs


class Play:
    def __init__(self):
        self.board = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
        ]
        self.red = [
            cs.Generals(cs.RED),
            cs.Advisors(cs.RED, cs.L),
            cs.Advisors(cs.RED, cs.R),
            cs.Elephants(cs.RED, cs.L),
            cs.Elephants(cs.RED, cs.R),
            cs.Horses(cs.RED, cs.L),
            cs.Horses(cs.RED, cs.R),
            cs.Chariots(cs.RED, cs.L),
            cs.Chariots(cs.RED, cs.R),
            cs.Cannons(cs.RED, cs.L),
            cs.Cannons(cs.RED, cs.R),
            cs.Soldiers(cs.RED, 0),
            cs.Soldiers(cs.RED, 2),
            cs.Soldiers(cs.RED, 4),
            cs.Soldiers(cs.RED, 6),
            cs.Soldiers(cs.RED, 8)
        ]
        self.black = [
            cs.Generals(cs.BLACK),
            cs.Advisors(cs.BLACK, cs.L),
            cs.Advisors(cs.BLACK, cs.R),
            cs.Elephants(cs.BLACK, cs.L),
            cs.Elephants(cs.BLACK, cs.R),
            cs.Horses(cs.BLACK, cs.L),
            cs.Horses(cs.BLACK, cs.R),
            cs.Chariots(cs.BLACK, cs.L),
            cs.Chariots(cs.BLACK, cs.R),
            cs.Cannons(cs.BLACK, cs.L),
            cs.Cannons(cs.BLACK, cs.R),
            cs.Soldiers(cs.BLACK, 0),
            cs.Soldiers(cs.BLACK, 2),
            cs.Soldiers(cs.BLACK, 4),
            cs.Soldiers(cs.BLACK, 6),
            cs.Soldiers(cs.BLACK, 8)
        ]
        for chessSet in [self.black, self.red]:
            for chess in chessSet:
                pos = chess.get_pos()
                if self.board[pos[0]][pos[1]] is None:
                    self.board[pos[0]][pos[1]] = chess
