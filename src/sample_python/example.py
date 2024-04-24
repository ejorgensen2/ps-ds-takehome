"""
Example main file for sample Python package.
"""

import os


def main() -> int:
    """
    Example function.

    Returns:
        int: Default run code.
    """
    print(f"Ran function <main> within <{os.path.realpath(__file__)}>")
    return 0


if __name__ == "__main__":
    main()
