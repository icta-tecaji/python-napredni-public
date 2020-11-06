def upper_converter(file_path: str):
    src_path, suffix = file_path.split(".")
    dest_path = f"{src_path}_upper.{suffix}"

    with open(file_path, "r") as reader:
        content = reader.read()

    with open(dest_path, "w") as witer:
        witer.write(content.upper())


if __name__ == "__main__":
    upper_converter("Del_03_Branje_in_pisanje_v_datoteke/data/test.txt")
