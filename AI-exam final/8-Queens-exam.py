from itertools import permutations
def solve_queens(n, max_solutions=5):
    sols = []
    for p in permutations(range(n)):
        if all(abs(p[i] - p[j]) != abs(i - j) for i in range(n) for j in range(i)):
            board = ['.' * c + 'Q' + '.' * (n - c - 1) for c in p]
            
            sols.append(board)
    return sols[:max_solutions], len(sols)
n = int(input("No of Queens: "))
max_out = int(input("Max solutions to show: "))
results, total = solve_queens(n, max_out)
print(f"\nTotal possible solutions for {n}-Queens: {total}\n")
for i, board in enumerate(results, 1):
    print(f"Solution {i}:")
    print('\n'.join(board), end="\n\n")