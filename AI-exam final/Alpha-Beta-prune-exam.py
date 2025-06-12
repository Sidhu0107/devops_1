def minimax(tree, alpha, beta, is_maximizing):
    if not isinstance(tree, list):
        return tree
    best = float('-inf') if is_maximizing else float('inf')
    for child in tree:
        value = minimax(child, alpha, beta, not is_maximizing)
        if is_maximizing:
            best = max(best, value)
            alpha = max(alpha, best)
        else:
            best = min(best, value)
            beta = min(beta, best)
        if alpha >= beta:
            break
    return best
tree = [[3, 5], [2, 9]]
print("Optimal value:", minimax(tree, float('-inf'), float('inf'), True))