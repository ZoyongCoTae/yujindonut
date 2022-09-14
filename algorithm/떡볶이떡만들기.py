import sys
input = sys.stdin.readline


def left_over(array, slice_int):
    sum = 0
    for x in array:
        if x > slice_int:
            sum += x - slice_int
    return sum


def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) / 2
        if left_over(array, mid) > target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


n, m = map(int, input().split())
dduk = list(map(int, input().split()))

dduk.sort()

print(binary_search(dduk, m, 0, dduk[-1]))
