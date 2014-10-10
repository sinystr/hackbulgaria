def nth_fib_lists(listA, listB, n):
    a = listA
    b = listB
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        count = 2
        max_count = n
        while count < max_count:
            count = count + 1
            old_a = a
            old_b = b
            a = old_b
            b = old_a + old_b
        return b
