#include <stdint.h>
#include <stdlib.h>

int64_t double_num(int64_t x)
{
    return x * 2;
}

void do_double_nums(int64_t *nums, int64_t count)
{
    for (int64_t i = 0; i < count; i++)
    {
        nums[i] = double_num(nums[i]);
    }
}

void do_double_nums_inline(int64_t *nums, int64_t count)
{
    for (int64_t i = 0; i < count; i++)
    {
        nums[i] = nums[i] * 2;
    }
}