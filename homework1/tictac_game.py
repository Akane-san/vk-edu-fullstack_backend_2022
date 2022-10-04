class TicTacGame:

    def __init__(self):
        self.board = []
        for row in range(3):
            self.board.append([])
            for _ in range(3):
                self.board[row].append('.')
        self.cross_count = 0

    def show_board(self):
        print(" ", end=" ")
        for j in range(1, 4):
            print(j, end=" ")
        print()
        for i in range(1, 4):
            print(i, end=" ")
            for j in range(1, 4):
                print(self.board[i-1][j-1], end=" ")
            print()

    def validate_input(self, coords):
        coordinates = coords.split()
        if len(coordinates) != 2:
            raise ValueError
        try:
            x = int(coordinates[0])
            y = int(coordinates[1])
            if not (1 <= x <= 3 and 1 <= y <= 3) or self.board[x-1][y-1] != '.':
                raise ValueError
        except ValueError:
            raise ValueError

    def start_game(self):
        print("Введите координаты хода,\nнапример: 1 3\nэто значит, что символ установится в 1 строке, 3 столбце")
        print("Ходит 1-й игрок")
        self.gamer_step(1)

    def gamer_step(self, gamer_num):
        print("Введите координаты")
        next_step_dict = {1: 2, 2: 1}
        gamer_sym = {1: "X", 2: "O"}
        next_gamer = next_step_dict[gamer_num]
        coords = input()
        try:
            self.validate_input(coords)
            x, y = [int(i) for i in coords.split()]
            self.board[x-1][y-1] = gamer_sym[gamer_num]
            if gamer_num == 1:
                self.cross_count += 1
            if self.cross_count == 5 and not self.check_winner(gamer_sym[gamer_num]):
                print("Игра закончена")
                print("Ничья!")
                self.show_board()
            elif self.cross_count > 2 and self.check_winner(gamer_sym[gamer_num]):
                print("Игра закончена")
                print(f"Выиграл {gamer_num} игрок!")
                self.show_board()
            else:
                self.show_board()
                print(f"Ходит {next_gamer}-й игрок")
                self.gamer_step(next_gamer)
        except ValueError:
            print("Координаты введены неправильно")
            self.gamer_step(gamer_num)

    def check_line(self, a1, a2, a3, smb):
        if a1 == smb and a2 == smb and a3 == smb:
            return True
        else:
            return False

    def check_winner(self, symbol):
        for n in range(3):
            if self.check_line(self.board[n][0], self.board[n][1], self.board[n][2], symbol) \
            or self.check_line(self.board[0][n], self.board[1][n], self.board[2][n], symbol):
                return True
        if self.check_line(self.board[0][0], self.board[1][1], self.board[2][2], symbol) \
            or self.check_line(self.board[2][0], self.board[1][1], self.board[0][2], symbol):
            return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
