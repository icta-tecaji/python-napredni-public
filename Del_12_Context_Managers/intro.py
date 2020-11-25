class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Revert:
    def __enter__(self):
        import sys

        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write

        return "AAAAAAAAAAABBBBBBBBBB"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys

        sys.stdout.write = self.original_write

        if exc_type is ZeroDivisionError:
            print("Ne deliti z nič v tem delu!!")
            return True


if __name__ == "__main__":
    # with open("Del_12_Context_Managers/data/hello.txt") as f:
    #     print(f.read())
    # with ManagedFile("Del_12_Context_Managers/data/hello.txt") as f:
    #     print(f.read())

    print("pytohn")
    with Revert() as a:
        print("danes")
        print(10 / 0)
        print(a)

    print("izven")
