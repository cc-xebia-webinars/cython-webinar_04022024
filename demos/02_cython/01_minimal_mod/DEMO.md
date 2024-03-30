# Cython: Minimal Module Demo

1. First, ensure the `python-class` Conda environment is activated. While the `cython` Conda package should be installed, if it is not, then install it.

```bash
python -m pip install cython
```

2. Create a new folder name `demo` and a `utils` subfolder.

```bash
mkdir -p demo/utils
```

3. In the `demo/utils` folder, create a new file named `utils.pyx`. The `.pyx` extension indicates that this file will be a Cython file. Add the following content to the file. When Cython compiles `utils.pyx`, a `utils.c` file is created.

```cython
print("Imported Utils")
```

4. In the `demo` folder, create a new file named `setup.py`. Add the following code to the file. The `cythonize` and `setup` function are used to compile the Cython file into a C file and then into a shared library.

```python
from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("./utils/utils.pyx"))
```

5. In the `demo` folder, create a new file named `Makefile`. Add the following content to the file.

```makefile
utils: ./utils/utils.pyx
	python setup.py build_ext --inplace

clean:
	rm *.so
	rm utils/utils.c
	rm -rf build
```

6. Build the project by running the following command.

```bash
make -B utils
```

7. Run the following code to verify the Cython extension built successfully.

```bash
python -c 'import utils'
```

The output the command should be:

```text
Imported Utils
```

7. Let's review the output the build process. First, the final product of the build is a shared library with an `.so` extension. This shared library is a Python extension that can be imported directly into Python. The source code for the extension is located `utils/utils.c`. Review the file and search for "PyInit_utils". Does this look familiar? We created code similar to this in the Python C Extensions part of the course.

