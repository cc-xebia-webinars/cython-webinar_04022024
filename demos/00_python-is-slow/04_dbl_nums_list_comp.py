# time python ./04_dbl_nums_list_comp_fn.py


def do_double_nums(nums: list[int]) -> list[int]:
    return [num * 2 for num in nums]


if __name__ == "__main__":
    count = 10**7
    nums = list(range(count))
    double_nums = []
    double_nums = do_double_nums(nums)
    # uncomment the following code to verify the results
    # running the assertions will slow down the script
    # assert len(double_nums) == count
    # assert sum(nums) == 49999995000000
    # assert sum(double_nums) == 99999990000000
