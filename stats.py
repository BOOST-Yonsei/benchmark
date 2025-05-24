#!/bin/python3

from itertools import batched, filterfalse
import re
from statistics import mean, median, stdev

def parse(path):
    '''
    Returns [Kernel[], Userspace[], Total[], MultiUser[]]
    '''
    res =[[] for _ in range(4)]
    time = re.compile(r"\d+.*?s")
    conv = re.compile(r"(\d+)*(?:min )*(\d+)\.(\d+)s")
    with open(path) as f:
        for run in batched(filterfalse(lambda line: len(line) < 2, f), 2):
            entry = [conv.findall(k)[0] for x in run for k in time.findall(x)]
            i = 0
            for m, s, ms in entry:
                t = 0 if m == '' else 60_000 * int(m)
                t += 1_000 * int(s) + int(ms)
                res[i].append(t)
                i += 1

    return res


def timereadable(ms):
    m, s = divmod(int(ms + 0.5), 60_000)
    s, ms = divmod(s, 1_000)

    sec = f"{s}.{ms:03}s"
    return sec if m == 0 else f"{m}min {sec}"

def printstat(data):
    print(f"Mean     = {timereadable(mean(data))}")
    print(f"Median   = {timereadable(median(data))}")
    print(f"Stdev    = {timereadable(stdev(data))}")
    print()


if __name__ == "__main__":
    from sys import argv

    kernel, user, total, multi = parse(argv[1])

    print("Kernel statistics")
    printstat(kernel)

    print("Userspace statistics")
    printstat(user)

    print("Total statistics")
    printstat(total)

    print("Multi-user statistics")
    printstat(multi)

    print("-" * 50)
    print("Kernel time")
    print(kernel)
    print()

    print("Userspace time")
    print(user)
    print()

    print("Total time")
    print(total)
    print()

    print("Multi-user time")
    print(multi)
