def do_double_nums(nums: list[int]) -> list[int]:
    cdef long i = 0
    cdef long nums_length = len(nums)
    cdef list result = []

    for i in range(nums_length):
        result.append(nums[i] * 2)

    return result
