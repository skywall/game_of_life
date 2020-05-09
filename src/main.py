from src.model.board import Board


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def main():
    board = Board()
    board.load(read_file("../zygotes/2"))

    for it in range(10):
        board.next_gen()
        print(board)


if __name__ == '__main__':
    main()
