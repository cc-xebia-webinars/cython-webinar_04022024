# make
# time python ./dbl_nums_cfn.py

from ctypes import CDLL, c_int64

double_nums_lib = CDLL("./double_nums_lib.so")


def do_double_nums(nums: list[int]) -> list[int]:
    convert_to_int64_nums = c_int64 * len(nums)
    # this conversion makes a copy of the original list
    # which is why there is no "double_nums" variable
    int64_nums = convert_to_int64_nums(*nums)
    double_nums_lib.do_double_nums(int64_nums, len(nums))
    return list(int64_nums)


if __name__ == "__main__":
    count = 10**7
    nums = list(range(count))
    dbl_nums = do_double_nums(nums)
    # uncomment the following code to verify the results
    # running the assertions will slow down the script
    # assert len(dbl_nums) == count
    # assert sum(nums) == 49999995000000
    # assert sum(dbl_nums) == 99999990000000
