# make
# time python ./dbl_nums_c_ext.py

from double_nums import create_double_nums

if __name__ == "__main__":
    count = 10**7
    nums = list(range(count))
    double_nums = create_double_nums(nums)
    # uncomment the following code to verify the results
    # running the assertions will slow down the script
    # assert len(double_nums) == count
    # assert sum(nums) == 49999995000000
    # assert sum(double_nums) == 99999990000000
