show = lambda b: print('\n'.join(' | '.join(b[i:i+3]) for i in (0, 3, 6)),'-' * 9,sep='\n')
board = [' '] * 9
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)]
player = 'X'
for _ in range(9):
    show(board)
    r, c = map(int, input(f"{player}'s move (row col): ").split())
    idx = 3 * r + c
    if board[idx] != ' ':
        print("❌ Taken! Try again.")
        continue
    board[idx] = player
    if any(board[a] == board[b] == board[c] != ' ' for a, b, c in wins):
        show(board)
        print(f"🏆 {player} wins!")
        break
    player = 'O' if player == 'X' else 'X'
else:
    show(board)
    print("🤝 It's a tie!")