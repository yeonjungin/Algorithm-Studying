s = list(input())
t = list(input())


def find(t):
    if len(t) == len(s):
        return t == s

    if t[0] == 'B' and find(t[:0:-1]):
        return True
    if t[-1] == 'A' and find(t[:-1]):
        return True


print(1 if find(t) else 0)