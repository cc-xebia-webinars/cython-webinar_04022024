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
