from collections import deque
def solve(j1, j2, target):
    q, v = deque([(0, 0)]), set()
    while q:
        a, b = q.popleft()
        if (a, b) in v: continue
        v.add((a, b))
        print(f"Jug1: {a}L, Jug2: {b}L")
        if a == target or b == target: return "✅ Target Reached!"
        q.extend([(j1, b), (a, j2), (0, b), (a, 0), 
                  (a - min(a, j2 - b), b + min(a, j2 - b)), 
                  (a + min(b, j1 - a), b - min(b, j1 - a))])
    return "❌ No solution"
print(solve(4, 3, 2))