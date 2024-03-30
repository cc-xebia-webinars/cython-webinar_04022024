# Cython Functions

In Cython, there are three main types of functions that you can define, each with its own purpose and characteristics: `def`, `cdef`, and `cpdef`. These keywords determine how the function is implemented and how it interacts with both Python and C code.

1. **`def` Functions**:
   - **Purpose**: These functions are meant to be used from Python code. They have the same behavior and capabilities as regular Python functions. They are slower than `cdef` functions because they involve Python overhead.
   - **Characteristics**:
     - Can use any Python data type and objects.
     - Support dynamic typing and polymorphism.
     - Involve Python function call overhead.
     - Suitable for public interfaces or when interacting with Python code.

   ```cython
   def py_func(arg1, arg2):
       # Python-level code
       return arg1 + arg2
   ```

2. **`cdef` Functions**:
   - **Purpose**: These functions are used for low-level C-like operations and are not meant to be called directly from Python code. They provide better performance by avoiding Python overhead.
   - **Characteristics**:
     - Can use C data types and objects, typed memory views, and NumPy arrays.
     - Involve minimal function call overhead (C-like function calls).
     - Not visible from Python code.
     - Useful for performance-critical operations within Cython code.

   ```cython
   cdef int c_func(int arg1, int arg2):
       # C-level code
       return arg1 + arg2
   ```

3. **`cpdef` Functions**:
   - **Purpose**: These functions provide a bridge between Python and C by generating both a `def` and a `cdef` version of the function. This allows the function to be called from both Python and Cython code.
   - **Characteristics**:
     - Generates a Python wrapper for the `cdef` function.
     - Can be called from both Python and Cython code.
     - Offers a compromise between flexibility (Python interface) and performance (Cython implementation).
     - Suitable for functions that need to be used both within Cython and from Python.

   ```cython
   cpdef int cp_func(int arg1, int arg2):
       # Common logic that works at both Python and C levels
       return arg1 + arg2
   ```

When writing Cython code, it's essential to consider the trade-offs between these function types. If you need the best performance within Cython code, use `cdef` functions. If you want an interface accessible from both Python and Cython, use `cpdef` functions. And if you're dealing with general Python code or public APIs, use `def` functions.