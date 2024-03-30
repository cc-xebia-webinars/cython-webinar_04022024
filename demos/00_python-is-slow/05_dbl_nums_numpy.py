# time python ./05_dbl_nums_numpy.py

import numpy as np


if __name__ == "__main__":
    count = 10**7
    nums = np.arange(count)
    double_nums = nums * 2
    # uncomment the following code to verify the results
    # running the assertions will slow down the script
    # assert len(double_nums) == count
    # assert sum(nums) == 49999995000000
    # assert sum(double_nums) == 99999990000000
