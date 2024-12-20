def solve():
    t = int(input())
    for _ in range(t):
        m, a, b, c = map(int, input().split())
        total = min(a, m) + min(b, m) + min(c, 2 * m - min(a, m) - min(b, m))
        print(total)

solve()
