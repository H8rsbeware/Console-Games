import tfe

def main():
    b = tfe.board()
    b.changeTile(1,1,2)
    b.changeTile(1,2,10)
    b.printBoard()

    print(str(b.findTiles()))


if __name__ == "__main__":
    main()
