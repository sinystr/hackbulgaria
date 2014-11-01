def f(l, s):
    return s == 0 or l != [] and (f(l[1:], s) or f(l[1:], s - l[0]))


print(f([2,2,3], 4))
