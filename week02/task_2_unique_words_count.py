from task_1_count_words import count_words


def unique_count_words(arr):
    unique_words = 0
    for i in count_words(arr):
        if(count_words(arr)[i] == 1):
            unique_words += 1

    return unique_words
