# first_last_occurrence.py

from binary_search import binary_search

def find_first_last_occurrence(arr, target):
    first_occurrence = binary_search(arr, target)

    if first_occurrence == -1:
        return -1, -1

    last_occurrence = first_occurrence
    while last_occurrence + 1 < len(arr) and arr[last_occurrence + 1] == target:
        last_occurrence += 1

    return first_occurrence, last_occurrence

