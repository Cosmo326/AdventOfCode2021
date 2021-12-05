from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
        #                   "",
        #                   "22 13 17 11  0",
        #                   " 8  2 23  4 24",
        #                   "21  9 14 16  7",
        #                   " 6 10  3 18  5",
        #                   " 1 12 20 15 19",
        #                   "",
        #                   " 3 15  0  2 22",
        #                   " 9 18 13 17  5",
        #                   "19  8  7 25 23",
        #                   "20 11 10 24  4",
        #                   "14 21 16 12  6",
        #                   "",
        #                   "14 21 17 24  4",
        #                   "10 16 15  9 19",
        #                   "18  8 23 26 20",
        #                   "22 11 13  6  5",
        #                   " 2  0 12  3  7"])

    def part1(self):
        selected = self.day_input[0].split(",")
        boards = []
        for board_index in range(1, len(self.day_input), 6):
            board_setup = self.day_input[board_index + 1:board_index + 6]
            bingo_board = BingoBoard(board_setup)
            boards.append(bingo_board)

        for number in selected:
            for board in boards:
                score = board.mark(int(number))
                if score != -1:
                    return score

    def part2(self):
        selected = self.day_input[0].split(",")
        boards = []
        skipped_boards = []
        last_score = 0
        for board_index in range(1, len(self.day_input), 6):
            board_setup = self.day_input[board_index + 1:board_index + 6]
            bingo_board = BingoBoard(board_setup)
            boards.append(bingo_board)

        for number in selected:
            for board in boards:
                skip = False
                for skipped_board in skipped_boards:
                    if skipped_board == board:
                        skip = True

                if skip:
                    continue

                score = board.mark(int(number))
                if score != -1:
                    skipped_boards.append(board)
                    last_score = score

        return last_score


class BingoBoard:
    def __init__(self, line_array):
        self.board = []
        self.marked = [[False, False, False, False, False],
                  [False, False, False, False, False],
                  [False, False, False, False, False],
                  [False, False, False, False, False],
                  [False, False, False, False, False]]
        self.total = 0

        for line in line_array:
            board_line = [int(line[:2].strip(" ")), int(line[3:5].strip(" ")), int(line[6:8].strip(" ")), int(line[9:11].strip(" ")), int(line[12:].strip(" "))]
            self.total += int(line[:2].strip(" ")) + int(line[3:5].strip(" ")) + int(line[6:8].strip(" ")) + int(line[9:11].strip(" ")) + int(line[12:].strip(" "))
            self.board.append(board_line)

    def is_winner(self):
        winner = False
        for index in range(5):
            if (self.marked[index][0] and self.marked[index][1] and self.marked[index][2] and self.marked[index][3] and self.marked[index][4]) or (self.marked[0][index] and self.marked[1][index] and self.marked[2][index] and self.marked[3][index] and self.marked[4][index]):
                winner = True

        return winner

    def mark(self, value):
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == value:
                    self.marked[y][x] = True
                    self.total -= value

        if self.is_winner():
            return self.total * value

        return -1

    def debug(self):
        print(self.board)
        print(self.total)
        print(self.marked)
        print()
