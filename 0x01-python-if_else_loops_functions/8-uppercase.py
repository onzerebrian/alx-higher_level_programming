#!/usr/bin/python3
def uppercase(str):
    for mm in str:
        print("{}".format(chr(ord(mm) - 32)
                          if (ord(mm) >= ord("a") and
                              ord(mm) <= ord("z")) else mm), end="")
    print()
