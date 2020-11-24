import functools


def remove_public_ips(func):
    @functools.wraps(func)
    def wrapper_remove_public_ips(*args, **kwargs):
        text = func(*args, **kwargs)
        clean_text = []
        for line in text:
            line_splited = line.split()
            src_ip = line_splited[5]
            if not (src_ip.startswith("192.168") or src_ip.startswith("10.")):
                line_splited[5] = "XXX.XXX.XXX.XXX"
                clean_line = " ".join(line_splited)
                clean_text.append(clean_line)
            else:
                clean_text.append(line)
        return clean_text

    return wrapper_remove_public_ips
