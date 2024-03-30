from double_nums_mod import do_double_nums

if __name__ == "__main__":
    count = 10**7
    nums = list(range(count))
    dbl_nums = do_double_nums(nums)
    # assert len(dbl_nums) == count
    # assert sum(nums) == 49999995000000
    # assert sum(dbl_nums) == 99999990000000
