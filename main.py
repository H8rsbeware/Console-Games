import tfe

def main():
    b = tfe.board()
    b.changeTile(1,1,2)
    b.changeTile(1,2,10)
    b.changeTile(2,3,3)
    b.printBoard()

    print(str(b.findTiles()))

    print("\n")
    b.Vslide(True)
    b.printBoard()

if __name__ == "__main__":
    main()
