if __name__ == "__main__":
    # Don’t compare boolean values to True or False using the equivalence operator.
    # Not recommended
    # my_bool = 6 > 5
    # if my_bool == True:
    #     return "6 is bigger than 5"

    # # Recommended
    # if my_bool:
    #     return "6 is bigger than 5"

    # Use the fact that empty sequences are falsy in if statements.
    # Not recommended
    my_list = []
    if not len(my_list) == 0:
        print("List is empty!")

    # Recommended
    my_list = []
    if not my_list:
        print("List is empty!")
