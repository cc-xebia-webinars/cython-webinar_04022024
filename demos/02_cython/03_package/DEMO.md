# Cython: Create a PyPi Package with Cython Source Code

1. Ensure the latest version of the following PyPi packages are installed.

    ```bash
    python -m pip install --upgrade pip setuptools wheel build
    ```

2. Copy the `demo_start` folder to `demo`. Perform all programming and commands from the `demo` folder.

    ```bash
    cp -R demo_start demo
    ```

3. The `cython` PyPi package will be needed to build the module. Update the `pyproject.toml` file to include `cython`.

    ```toml
    [build-system]
    requires = ["setuptools", "cython"]
    ```

4. The `setup.py` includes only the `cythonize` function call. Other project information such as the package name, version, and description are missing. While the `setup.py` file can be updated with this information (as shown earlier in the course) another option for defining this information is the `pyproject.toml` file. There are three places where such information can be stored: `setup.py`, `pyproject.toml`, and `setup.cfg`. Add the following content to the end of the `pyproject.toml` file.

    ```toml
    [project]
    name = "utils"
    version = "1.0.0"
    description = "Common Utilities"
    authors = [
        {name = "Eric Greene", email = "eric@cloudcontraptions.com"},
    ]
    ```

    > **Note:** There are three places where package metadata can be configured: `setup.py`, `pyproject.toml`, and `setup.cfg`. The option you choose depends upon the project. Older projects will use `setup.py`. Newer projects will be use `pyproject.toml` or `setup.cfg`. For Conda packages with `meta.yaml ` files using Jinja2 templating, `setup.py` is used.

5. Update the `setup.py` project to allow `build` module to load the source Cython files. The `build` module will detect the presence of the `cython` package, and run the `*.pyx` files through the Cython compiler.

    ```python
    from setuptools import Extension, setup


    def main() -> None:
        setup(
            ext_modules=[
                Extension(
                    name="utils",
                    sources=["./utils/utils.pyx"],
                )
            ],
        )


    if __name__ == "__main__":
        main()
    ```

6. From the terminal, within the `part_01` folder, run the `build` module to create the wheel.

    ```bash
    python -m build
    ```

7. Install the `utils` wheel package into the global Python environment.

    ```bash
    python -m pip install --no-deps ./dist/*.whl
    ```

8. Run the following command to verify the package works.

    ```bash
    python -c 'import utils; print(utils.add(1,2))'
    ```

    Verify the output looks like this:

    ```text
    3.0
    ```

10. Uninstall the `utils` package from the global Python environment.

    ```bash
    python -m pip uninstall -y utils
    ```
