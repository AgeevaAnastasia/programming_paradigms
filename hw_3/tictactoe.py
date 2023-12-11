# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

# Реализуем задачу в парадигме ООП, поскольку для написания игр
# данная парадигма является наиболее подходящей

class TicTacToe:
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def draw_board(self) -> None:
        print('-------------')
        for row in self.board:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print('\n-------------')

    def make_move(self, row: int, col: int) -> bool:
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self, player: str) -> bool:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player or \
                    self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def play(self) -> None:
        while True:
            self.draw_board()
            print('Сейчас ходит', self.current_player)
            row = int(input('Введите номер строки (1-3): ')) - 1
            col = int(input('Введите номер столбца (1-3): ')) - 1

            if row < 0 or row > 2 or col < 0 or col > 2:
                print('Неверная ячейка, введите координаты еще раз.')
                continue

            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.draw_board()
                    print('Игрок', self.current_player, 'победил!')
                    break

                if all(cell != ' ' for row in self.board for cell in row):
                    self.draw_board()
                    print('Ничья!')
                    break

            else:
                print('Эта клетка уже занята. Попробуйте другую.')


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
