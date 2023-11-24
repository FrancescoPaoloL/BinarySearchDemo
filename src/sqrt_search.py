# sqrt_search.py

def mySqrt(x):
    if x < 0:
        return -1

    left, right = 0, x

    while left <= right:
        mid = left + (right - left) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

