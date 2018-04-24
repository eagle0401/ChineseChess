import ChineseChess.chessObject as cs


def __init__(self):
    self.borad = [[None]*9]*10
    self.red = [
        cs.Generals(cs.RED),
        cs.Advisors(cs.RED, cs.L),
        cs.Advisors(cs.RED, cs.R),
        cs.Elephants(cs.RED, cs.L),
        cs.Elephants(cs.RED, cs.R),
        cs.Horses(cs.RED, cs.L),
        cs.Horses(cs.RED, cs.R),
    ]
