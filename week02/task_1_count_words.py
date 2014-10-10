def count_words(arr):
    unique_arr = []
    words_dict = {}

    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    for i in unique_arr:
        words_dict[i] = arr.count(i)
    return words_dict
