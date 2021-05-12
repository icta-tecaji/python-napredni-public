import os


def read_text_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = file.read()
    return data


def get_current_file_path(file_name) -> str:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    full_file_path = f"{current_dir}/{file_name}"
    return full_file_path


if __name__ == "__main__":
    file_path = get_current_file_path("test.txt")
    my_data = read_text_file(file_path)
    print(my_data)
