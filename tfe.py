# A recreation of the game 2048

class board:
    def __init__(self):
        self.memory = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.size = 4

    # Formats the board, and changes memory into corresponding digit
    def printBoard(self):
        for row in self.memory:
            ln : str = ""
            for tile in row:
                p : int = pow(2, tile)
                if p != 1:
                    ln += str(p)
                    i = 0
                    while i < 5 - len(str(p)):
                        ln += " "
                        i += 1
                else:
                    ln += "0    "
            print(ln)

    def changeTile(self, r, c, v):
        self.memory[r][c] = v

    def findTiles(self):
        res : list = []

        row = 0
        while row < self.size:
            col = 0
            while col < self.size:
                if self.memory[row][col] != 0:
                    res.append((row,col))
                col += 1
            row += 1

        return res

    def isEmpty(self, r, c):
        if self.memory[r][c] != 0:
            return False
        else:
            return True

    def getMemory(self, r, c):
        return self.memory[r][c]

    def Vslide(self, up:bool):



        # Bug, up doesnt push up multiple times
        while True:
            tiles = self.findTiles()
            for tile in tiles:
                if tile[0] == 0 or tile[0] == self.size - 1:
                    return
                if up:
                    if self.isEmpty(tile[0]-1,tile[1]):
                        m = self.getMemory(tile[0], tile[1])
                        self.changeTile(tile[0]-1,tile[1],m)
                        self.changeTile(tile[0], tile[1], 0)

                if not up:
                    if self.isEmpty(tile[0]+1, tile[1]):
                        m = self.getMemory(tile[0], tile[1])
                        self.changeTile(tile[0]+1, tile[1],m)
                        self.changeTile(tile[0],tile[1],0)





    def Hslide(self):
        r = 0
        c = 0

