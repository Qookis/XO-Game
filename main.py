print('Добро пожаловать в игру крестики нолики')
print('_______________________________________')
print('Чтобы играть в эту игру нужно')
print('указать сначла номер строки,')
print('а потом номер столбца')
print('_______________________________________')

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print('|'.join(row))

def check_win(player):
    # Проверка строк
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Проверка столбцов
    for col in range(3):
        if all([row[col] == player for row in board]):
            return True

    # Проверка диагоналей
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

player = 'X'
while True:
    print_board()
    row = int(input(f'{player}, Выбери строку от 0 до 2): '))
    col = int(input(f'{player}, Выбери столбец от 0 до 2: '))
    if board[row][col] != ' ':
        print('ячейка занята')
        continue
    board[row][col] = player
    if check_win(player):
        print(f'{player} выиграл!')
        break
    player = 'O' if player == 'X' else 'X'
