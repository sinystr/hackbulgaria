from task_9_fobonaccis_list import nth_fib_lists


def member_of_nth_fib_lists(listA, listB, needle):
    nth_fibonnaci = []
    counter = 1
    while len(nth_fibonnaci) < len(needle):
        nth_fibonnaci = nth_fib_lists(listA, listB, counter)
        counter += 1
        if nth_fibonnaci == needle:
            return True
    return False
