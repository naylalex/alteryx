#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    print("Name is required.")
    quit()

print("Hello {}".format(name))

