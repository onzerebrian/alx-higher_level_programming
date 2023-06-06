#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if (b > a):
            print("{}{}".format(a, b), end="")
            if (a < 8):
                print(", ", end="")
print("\n", end="")
