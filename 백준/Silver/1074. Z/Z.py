def Z(n, x, y, r, c):
    if n == 1:
        if r == 0:
            if c == 0:
                return 0
            else:
                return 1
        else:
            if c == 0:
                return 2
            else:
                return 3

    else:
        if r < 2 ** (n - 1) and c < 2 ** (n - 1):
            return Z(n - 1, x, y, r, c)
        elif r < 2 ** (n - 1) and c >= 2 ** (n - 1):
            y += 2 ** (n - 1)
            c -= 2 ** (n - 1)
            return 2 ** ((n - 1) * 2) + Z(n - 1, x, y, r, c)
        elif r >= 2 ** (n - 1) and c < 2 ** (n - 1):        
            x += 2 ** (n - 1)
            r -= 2 ** (n - 1)
            return (2 ** ((n - 1) * 2)) * 2 + Z(n - 1, x, y, r, c)
        elif r >= 2 ** (n - 1) and c >= 2 ** (n - 1):
            x += 2 ** (n - 1)
            y += 2 ** (n - 1)
            r -= 2 ** (n - 1)
            c -= 2 ** (n - 1)
            return (2 ** ((n - 1) * 2)) * 3 + Z(n - 1, x, y, r, c)

N, r, c = map(int, input().split())

result = Z(N, 0, 0, r, c)

print(result)