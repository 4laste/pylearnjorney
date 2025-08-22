def reverse_string(s):
    return s[::-1]

strerror = "must be revers"
assert reverse_string([1, 2, 3]) == [3, 2, 1], strerror
assert reverse_string("abc") == "cba", strerror
