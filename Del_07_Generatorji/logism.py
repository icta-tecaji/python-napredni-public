import random
import time

from data import docs, ips

with open("./data/access-log", "w") as f:
    while True:
        time.sleep(random.random())
        n = random.randint(0, len(ips) - 1)
        m = random.randint(0, len(docs) - 1)
        t = time.time()
        date = time.strftime("[%d/%b/%YT%H:%M:%S -0600]", time.localtime(t))
        write_string = f"{ips[n]} - - {date} {docs[m]}\n"
        f.write(write_string)
        f.flush()
