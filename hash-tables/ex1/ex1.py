#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize,
                        hash)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 1:
        answer = None

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    for i, weight in enumerate(weights):
        first = weight
        second = limit - first
        result = hash_table_retrieve(ht, second)

        if result is not None:
            if result > i:
                answer = (result, i)
            elif result < i:
                answer = (i, result)


    return print_answer(answer)


def print_answer(answer):
    if answer is not None:
        print(f"{answer[0]} {answer[1]}")
        return answer
    else:
        print("None")