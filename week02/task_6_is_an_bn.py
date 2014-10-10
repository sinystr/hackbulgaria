def is_an_bn(word):
    if len(word) == 0 or len(word) % 2 != 0:
        return False

    for i in range(0, len(word) // 2):
        if word[i] != 'a' or word[-i-1] != 'b':
            return False

    return True
