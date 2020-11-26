import os


def example1():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    current_path = os.getcwd()
    return current_path


if __name__ == "__main__":
    print(f"Current Directory: {example1()}")
