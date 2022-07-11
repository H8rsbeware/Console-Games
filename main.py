import tfe

def main():
    b = tfe.board()
    b.changeTile(1,1,2)
    b.changeTile(0,2,10)
    b.changeTile(2,2,2)
    b.printBoard()

    print(str(b.findTiles()))

    print("\n")
    b.vSlide(False)
    b.printBoard()
    print("\n")
    b.hSlide(True)
    b.printBoard()
    print("\n")
    b.merge("w")
    b.printBoard()



if __name__ == "__main__":
    main()
