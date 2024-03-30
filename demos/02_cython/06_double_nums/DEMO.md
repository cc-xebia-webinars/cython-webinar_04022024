# Cython: Double Nums Performance

1. Open a terminal window, and change to the `07_double_nums` folder.

2. Make the `double_nums_mod` Cython module.

    ```bash
    make -B
    ```

3. Run the `app.py` file the `time` program.

    ```bash
    time python ./app.py
    ```

4. Review the performance of the different methods.

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
    | Cython | 0m0.687s | Uses a real Python list, and is much faster that the earlier Python list examples, but still much slower than C or Numpy which used better array data structures. |

## Conclusion

The value of Cython and C extensions is where there is a lot of computationally intensive code that can be optimized.  The overhead of converting data between Python and C memory structures can be significant so performance improve of the computations against the data conversions must be considered. If possible, avoid Python lists when working with large datasets and use Numpy arrays which can be passed to C without the conversion overhead.