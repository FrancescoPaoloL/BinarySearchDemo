# main.py

from binary_search import binary_search
from first_last_occurrence import find_first_last_occurrence
from search_2d_matrix import search_in_2d_matrix
from sqrt_search import mySqrt

def main():
    # Finding the square root of a number
    number = 25
    sqrt_result = mySqrt(number)
    print(f"The square root of {number} is approximately {sqrt_result}")

    # Finding the first and last occurrence of an element in a sorted array
    sorted_array = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
    target_element = 4
    first, last = find_first_last_occurrence(sorted_array, target_element)
    print(f"Sorted Array: {sorted_array}")
    print(f"First occurrence of {target_element}: {first}, Last occurrence: {last}")

    # Searching in a 2D matrix
    sorted_matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target_value = 16
    is_present = search_in_2d_matrix(sorted_matrix, target_value)
    print(f"Sorted Matrix:")
    for row in sorted_matrix:
        print(row)
    print(f"Is {target_value} present in the 2D matrix? {is_present}")

    # Finding the peak element in an array
    peak_array = [1, 3, 20, 4, 1, 0]
    peak_index = binary_search(peak_array, max(peak_array))
    print(f"Array: {peak_array}")
    print(f"The peak element in the array is {peak_array[peak_index]} at index {peak_index}")

if __name__ == "__main__":
    main()

