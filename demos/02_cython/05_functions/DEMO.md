# Cython: Work with Functions

1. Ensure the latest version of the following PyPi packages are installed.

    ```bash
    python -m pip install --upgrade pip cython
    ```

2. Create a new folder named `demo`. Do all programming and command line work in the `demo` folder.

    ```bash
    mkdir demo
    ```

3. In the `demo` folder, create new file named `setup.py`. Add the following code to the file.

    ```python
    from distutils.core import setup
    from Cython.Build import cythonize

    setup(ext_modules=cythonize("./double_nums_mod.pyx"))
    ```

4. In the `demo` folder, create a new file named `double_nums_mod.pyx` file. Add the following code to the file.

    ```cython
    def double_num(num: int) -> int:
        return num * 2

    def do_double_nums(nums: list[int]) -> list[int]:
        cdef int num
        cdef list result = []

        for num in nums:
            result.append(double(num))

        return result
    ```

5. In the `demo` folder, create a new file named `app.py` file. Add the follow code to the file.

    ```python
    from double_nums_mod import do_double_nums


    def main() -> None:
        print(do_double_nums(range(5)))


    if __name__ == "__main__":
        main()
    ```

6. In the `demo` folder, create a new file named `Makefile` file. Add the follow code to the file.

    ```makefile
    double_nums_mod: ./double_nums_mod.pyx
        python setup.py build_ext --inplace


    clean:
        rm -f *.so
        rm -f *.c
        rm -rf build
    ```

7. Build the Cython extension module.

    ```bash
    make -B
    ```

8. Run the application.

    ```bash
    python app.py
    ```

    The output will be the following:

    ```text
    [0, 2, 4, 6, 8]
    ```

9. Open the `double_nums_mod.c` file to see the generated C code. Search for the text `__pyx_pf_15double_nums_mod_2do_double_nums`, three results will be returned. View the last result. Scroll down to the `PyMethod_GET_FUNCTION` function call.

    ```c
    PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
    ```

    On the first iteration, the Python `double_num` function is retrieved. On each iteration, the function is called:

    ```c
    __pyx_t_3 = __Pyx_PyObject_FastCall(__pyx_t_5, __pyx_callargs+1-__pyx_t_4, 1+__pyx_t_4);
    ```

    The `PyObject_FastCall` function is a Python C-API function that calls a Python function in a optimized manner relative to `PyObject_Call` and `PyObject_CallFunction`. While `PyObject_FastCall` is optimized it is still slower than a C function call.

10. When defining functions in Cython, functions can take one of three forms:

    - `def`: Normal Python Function, can be called from Python
    - `cdef`: C-only Function, cannot be called from Python
    - `cpdef`: Generates both `def` and `cdef` functions

    The C-only function is the fastest, because it does not use Python's dynamic typing and polymorphism.

    Update the `double_nums_mod.pyx` file to have the following code for the `double_num` and `do_double_nums` function.

    ```cython
    cdef int double_num(int num):
        return num * 2

    def do_double_nums(nums: list[int]) -> list[int]:
        cdef int num
        cdef list result = []

        for num in nums:
            result.append(double_num(num))

        return result
    ```

11. Build and run the Cython extension module.

    ```bash
    make -B
    ```

    ```bash
    python app.py
    ```

    The output will be the following:

    ```text
    [0, 2, 4, 6, 8]
    ```

12. Open the `double_nums_mod.c` file to see the generated C code. Search for the text `__pyx_pf_15double_nums_mod_2do_double_nums`, three results will be returned. View the last result. Scroll down to the `__pyx_f_15double_nums_mod_double_num` function call.

    ```c
    __pyx_t_4 = __pyx_f_15double_nums_mod_double_num(__pyx_v_num);
    ```

    Instead of calling a Python function, now a C function is being called.

    ```c
    static int __pyx_f_15double_nums_mod_double_num(int __pyx_v_num) {
      int __pyx_r;
      __pyx_r = (__pyx_v_num * 2);
      goto __pyx_L0;
      __pyx_L0:;
      return __pyx_r;
    }
    ```

13. Calling a C function will always be faster than calling a Python function. Let's update the `double_nums_mod.pyx` file to use the `cpdef` keyword.

    ```cython
    cpdef int double_num(int num):
        return num * 2

    def do_double_nums(nums: list[int]) -> list[int]:
        cdef int num
        cdef list result = []

        for num in nums:
            result.append(double_num(num))

        return result
    ```

14. Open the `double_nums_mod.c` file to see the generated C code. Search for the text `__pyx_pf_15double_nums_mod_2do_double_nums`, three results will be returned. View the last result. Scroll down to the `__pyx_f_15double_nums_mod_double_num` function call. In the function implementation,  which `double_num` function is called the C function or the Python?

15. Do a search for `__pyx_f_15double_nums_mod_double_num`. This version of the `double_nums` function will be C code. Now do a search for `__pyx_pf_15double_nums_mod_double_num` for the Python version of the function. The `cpdef` keyword generates both a C and Python function.
