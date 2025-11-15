def movesToStamp(stamp, target):
    s = list(target)
    m, n = len(stamp), len(target)
    res = []
    total = 0
    changed = True
    used = [False] * n

    def can_replace(i):
        replaced = 0
        for j in range(m):
            if s[i+j] != '?' and s[i+j] != stamp[j]:
                return 0
            if s[i+j] != '?':
                replaced += 1
        return replaced

    while changed:
        changed = False
        for i in range(n - m, -1, -1):   
            if not used[i]:
                replaced = can_replace(i)
                if replaced > 0:
                    for j in range(m):
                        s[i+j] = '?'
                    used[i] = True
                    changed = True
                    total += replaced
                    res.append(i)
                    if total == n:
                        return res[::-1]

    return []


print(movesToStamp("abc", "ababc"))
print(movesToStamp("abca", "aabcaca"))