# Getting Started

## Learning Objectives

- Think more critically about Python code
- Understand that equivalent functionality/algorithm does not meaning equivalent performance
- Explore why Python code is slow
- Learn about and select between options to improve Python performance

### Quick Profiling with the Time Command

The `time` command in Unix-like operating systems is used to measure the execution time of a command or a process. It provides information about the real time, user CPU time, and system CPU time consumed by the command or process.

When you run the `time` command followed by another command, the output will include three main metrics:

1. **Real Time**: This is the actual time that has elapsed from the moment the command started to the moment it finished. It includes all kinds of delays, such as waiting for input/output operations or system load. The real time is a good measure of how long the command took to complete in terms of wall-clock time.

2. **User CPU Time**: This is the amount of CPU time consumed by the command in user-mode code. It represents the time spent executing your program's code (user code) as opposed to system-level operations. It includes the time your program spent using the CPU for computation.

3. **System CPU Time**: This is the amount of CPU time consumed by the command in kernel-mode code. It represents the time spent executing code within the operating system itself, such as handling system calls, interrupts, and managing memory and processes.

Here's an example of using the `time` command and interpreting its outputs:

```bash
$ time ls -l

real    0m0.035s
user    0m0.004s
sys     0m0.008s
```

In this example, the `ls -l` command is used to list files in the current directory. The `time` command output provides the following information:

- `real`: The real time taken by the command. In this case, it's approximately 0.035 seconds.
- `user`: The user CPU time consumed by the command. It's the time spent executing your program's code, which is approximately 0.004 seconds.
- `sys`: The system CPU time consumed by the command. It's the time spent in kernel-mode code, which is approximately 0.008 seconds.

Keep in mind that the actual values might vary based on the system's load, the specific command being executed, and other factors. The real time is typically the highest value since it includes all delays and overheads, while the sum of user and sys times might be less than the real time if the system is multitasking or the command spends time waiting for I/O.

Overall, the `time` command helps you assess the performance and resource utilization of a command or process in terms of time spent on different aspects of execution.

## Explore Some Simple Python Examples

**Note:** Do not focus on absolute numbers, focus on relative differences. These examples have been coded to run fast so they can be run multiple times quickly. You will see results center around numbers consistently. Look at the relative difference between the centers. Multiply by 10 to scale out the number to think about the larger differences at scale.

### 01: Manual List Creation and Appending with Function Call

```python
def double(num: int) -> int:
    return num * 2


def do_double_nums(nums: list[int]) -> list[int]:
    double_nums = []
    for num in nums:
        double_nums.append(double(num))
    return double_nums
```

Run the example: `time python ./01_dbl_nums_for_in_fn.py`

Results:

```text
real    0m1.646s
user    0m1.293s
sys     0m0.293s
```

### 02: Manual List Creation and Appending with Inline Expression

```python
def do_double_nums(nums: list[int]) -> list[int]:
    double_nums = []
    for num in nums:
        double_nums.append(num * 2)
    return double_nums
```

Run the example: `time python ./02_dbl_nums_for_in.py`

Results:

```text
real    0m1.081s
user    0m0.746s
sys     0m0.331s
```

### 03: List Creation with List Comprehension and Function Call

```python
def double(num: int) -> int:
    return num * 2


def do_double_nums(nums: list[int]) -> list[int]:
    return [double(num) for num in nums]
```

Run the example: `time python ./03_dbl_nums_list_comp_fn.py`

Results:

```text
real    0m1.491s
user    0m1.154s
sys     0m0.332s
```

### 04: List Creation with List Comprehension and Inline Expression

```python
def do_double_nums(nums: list[int]) -> list[int]:
    return [num * 2 for num in nums]
```

Run the example: `time python ./04_dbl_nums_list_comp.py`

Results:

```text
real    0m1.127s
user    0m0.751s
sys     0m0.328s
```

### 05: List Creation with Numpy

```python
nums = np.arange(count)
double_nums = nums * 2
```

Run the example: `time python ./05_dbl_nums_numpy.py`

Results:

```text
real    0m0.166s
user    0m0.124s
sys     0m0.114s
```

### 06: C Array

```c
void do_double_nums(int *nums, int *double_nums, int count)
{
    for (int i = 0; i < count; i++)
    {
        double_nums[i] = nums[i] * 2;
    }
}
```

Run the example:

```bash
make
time ./out/app
```

Results:

```text
real    0m0.038s
user    0m0.034s
sys     0m0.004s
```

### 07: CTypes: Call C Function from Python

```python
double_nums_lib = CDLL("./double_nums_lib.so")
```

```python
double_nums_lib.do_double_nums(int64_nums, len(nums))
```

Run the examples:

```bash
make
time python ./dbl_nums_cfn.py
```

-- or --

```bash
make
time python ./dbl_nums_cfn_inline.py
```

Results:

```text
real    0m2.357s
user    0m2.036s
sys     0m0.301s
```

### 08: CTypes & Numpy: Call C Function from Python

```python
double_nums_lib = CDLL("./double_nums_lib.so")
```

```python
def double_nums(nums: np.ndarray) -> np.ndarray:
    int64_double_nums = nums.copy()
    double_nums_lib.do_double_nums(int64_double_nums, int64_double_nums.size)
    return int64_double_nums
```

Run the examples:

```bash
make
time python ./dbl_nums_cfn_numpy.py
```

Results:

```text
real    0m0.178s
user    0m0.167s
sys     0m0.115s
```

## Quick Analysis

| Method | Time | Notes |
| --- | --- | --- |
| Manual List Creation and Appending with Function Call | 0m1.646s | Slowest method, function call slows down code. |
| Manual List Creation and Appending with Inline Expression | 0m1.081s | Faster, because function calls are slow. |
| List Creation with List Comprehension and Function Call | 0m1.491s | List comprehension is much faster than appending to the list. |
| List Creation with List Comprehension and Inline Expression | 0m1.127s | Optimize with comprehesion and no function call. |
| List Creation with Numpy | 0m0.166s | Use a package coded in optimized C with a Python wrapper.  |
| C Array | 0m0.038s | Pure C code, nothing beats this, but memory management is manual. |
| CTypes: Call C Function from Python | 0m2.357s | C code is used, but lots of time lost converting data from Python to C memory structures. |
| CTypes & Numpy: Call C Function from Python | 0m0.178s | Numpy uses a memory structure understood by C. |

#### Summary of Results

- List comprehension is somewhat faster than manual list creation and iteration in a for-in loop
- The call to the Python function to perform the doubling greatly slowed down both the list comprehension and for-in loop - Python function calls are expensive
- Using an optimized Python package like Numpy written in optimized C code is a lot faster than a normal Python list. Numpy is a little slower than a plain C program, but you the power of Python and near C speeds with something like Numpy
- While the C code alone is very fast, trying to call C code from Python in this case is not efficient because a lot of time is spent converting from the Python list to the C array and back again, CTypes are easy but may not be efficient
- Writing C code may seem tempting, but it is very easy to make mistakes with memory management in C, we need to find a fast solution that is quick to code, and has few security risks

#### Analysis

While all examples created the same double nums array using the same algorithmic approach, Python language features and code organization with functions impacted the performance results.

The goal of this course is to understand what impacts performance, why it impacts it, and the options we have as Python programmers to improve performance through Python code and C programming.