from sys import *

def verify_repeat(a = ""):
    for i in range(len(a)):
        for c in range(len(a)):
            if c != i and a[i] == a[c]:
                return 0
    return 1

def check_uppercase(s = ""):
    for l in s:
        if l not in "a"

def check_lowercase(s = ""):

if len(argv) > 1:
    if len(argv[1]) >= 10 and verify_repeat(argv[1]):
        print(f"\033[1;92m{argv[1]} - OK    {len(argv[1])}\033[0m")
    else:
        print(f"\033[1;91m{argv[1]} - KO    {len(argv[1])}\033[0m")
