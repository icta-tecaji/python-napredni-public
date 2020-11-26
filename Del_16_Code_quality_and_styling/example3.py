def identity(value):
    return value


def contains(container, value):
    if value in container:
        return True
    else:
        return False


def contains_all(container, values):
    for value in values:
        if not contains(container, value):
            return False
    return True
