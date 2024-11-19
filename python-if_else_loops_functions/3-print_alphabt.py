#!/usr/bin/python3
floors = list(range(97, 123))
floors.remove(101)
floors.remove(113)
for i in floors:
    print("{}".format(chr(i)), end="")
