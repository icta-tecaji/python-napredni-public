import re


def grep(pattern, lines):
    patc = re.compile(pattern)
    for line in lines:
        if patc.search(line):
            yield line


if __name__ == "__main__":
    from follow import follow

    with open("./data/access-log") as logfile:
        loglines = follow(logfile)

        # pylines = grep(r"python", loglines)

        total_sum = 0

        for line in loglines:
            # print(line)
            # print("--------------")
            bytes_column = line.rsplit(None, 1)[1]
            if bytes_column != "-":
                total_sum += int(bytes_column)

            print(total_sum)
