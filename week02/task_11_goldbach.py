from is_prime import is_prime


def goldbach(n):
    global_bach = []
    for i in range(1, n // 2):
        if is_prime(i) and is_prime(n-i):
            global_bach.append((i, n-i))
    return global_bach

