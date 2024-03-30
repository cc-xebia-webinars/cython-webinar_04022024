from ctypes import CDLL, c_int64
import numpy as np
from numpy.ctypeslib import ndpointer

double_nums_lib = CDLL("./double_nums_lib.so")

# annotate the function with specific types for the arugments and return value
double_nums_lib.do_double_nums.restype = None
double_nums_lib.do_double_nums.argtypes = [
    # Creates a new type using the ndpointer function from the numpy module.
    # The ndpointer function is used to create a C-compatible data type that
    # represents a pointer to a multi-dimensional array.
    ndpointer(c_int64, flags="C_CONTIGUOUS"),
    c_int64,
]


def double_nums(nums: np.ndarray) -> np.ndarray:
    # Create a copy of the nums array so the copy will be modified, not the
    # original array.
    int64_double_nums = nums.copy()

    # Calls the C function passing a C array and length, the array will
    # be modified in-place.
    double_nums_lib.do_double_nums(int64_double_nums, int64_double_nums.size)

    return int64_double_nums


if __name__ == "__main__":
    count = 10**7
    nums = np.arange(count, dtype=np.int64)
    dbl_nums = double_nums(nums)
    # uncomment the following code to verify the results
    # running the assertions will slow down the script
    # assert len(dbl_nums) == count
    # assert np.sum(nums) == 49999995000000
    # assert np.sum(dbl_nums) == 99999990000000
