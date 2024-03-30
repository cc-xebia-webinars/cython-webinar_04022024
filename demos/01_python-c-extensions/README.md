# Custom Python C Extension

## Build & Run

To build the C extension, run the `make` command. A `double_nums.so` will be created.

```bash
make
```

To run the code in the C extension, use Python to run `dbl_nums_c_ext.py` file. It will import the `so` file and call the extension `create_double_nums` method.

```bash
time python ./dbl_nums_c_ext.py
```

## Analysis

The custom Python C extension returns results that are better than plain Python, but not as performant as Numpy.

```text
real    0m0.747s
user    0m0.426s
sys     0m0.321s
```

Writing a C extension is a powerful way to improve Python application performance for custom algorithms. But, there are two potential problems with writing a C extension. First, the Python C API is complex. Learning the C API is more involved than using C Types. However, once learned, it is not that hard if the programmer has system-level programming experience. Second, memory management is manual so there are risks making mistakes allocating, deallocating, owning, borrowing memory. Third, because C code is very low-level and imperative, the programmer needs to know a lot of details to program an efficient algorithm.

If a third-party package such as Numpy is an option, it would be preferred because the low-level details such as memory management and efficient hardware use are covered.