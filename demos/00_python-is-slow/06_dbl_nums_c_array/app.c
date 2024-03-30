// make
// time ./out/app

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#define COUNT 10000000
#define SUM_NUMS 49999995000000
#define SUM_DOUBLE_NUMS 99999990000000

void init_nums(int *nums, int count)
{
    for (int i = 0; i < count; i++)
    {
        nums[i] = i;
    }
}

void do_double_nums(int *nums, int *double_nums, int count)
{
    for (int i = 0; i < count; i++)
    {
        double_nums[i] = nums[i] * 2;
    }
}

int main(void)
{
    int *nums = malloc(COUNT * sizeof(int));
    int *double_nums = malloc(COUNT * sizeof(int));

    init_nums(nums, COUNT);
    do_double_nums(nums, double_nums, COUNT);

    // uncomment to run assertions to verify the results
    // running this will make the program run slower
    // long sum_nums = 0;
    // long sum_double_nums = 0;
    // for (int i = 0; i < COUNT; i++)
    // {
    //     sum_nums += nums[i];
    //     sum_double_nums += double_nums[i];
    // }

    // assert(sum_nums == SUM_NUMS);
    // assert(sum_double_nums == SUM_DOUBLE_NUMS);

    free(nums);
    free(double_nums);

    return 0;
}