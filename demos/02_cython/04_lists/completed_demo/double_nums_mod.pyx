# def do_double_nums(nums):
#     result = []

#     for num in nums:
#         result.append(num * 2)

#     return result

# def do_double_nums(nums: list[int]) -> list[int]:
#     result: list[int] = []

#     for num in nums:
#         result.append(num * 2)

#     return result

# def do_double_nums(nums: list[int]) -> list[int]:
#     cdef int index = 0
#     cdef int count = len(nums)
#     cdef list result = []

#     for index in range(count):
#         result.append(nums[index] * 2)

#     return result


# def do_double_nums(nums: list[int]) -> list[int]:
#     return [num * 2 for num in nums]

cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def do_double_nums(nums: list[int]) -> list[int]:
    cdef int index = 0
    cdef int count = len(nums)
    cdef list result = []

    for index in range(count):
        result.append(nums[index] * 2)

    return result