#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 22, 2022
# This program uses a loop an if statement
# to display integers from 1000 - 2000.
# It puts multiples of 5 on a new line.

def main():
    # loop to increment counter
    for counter in range(1000, 2001):
        if counter == 1000:
            # to avoid an empty newline at the beginning of program
            print(counter, " ", end="")
        elif counter % 5 == 0:
            # to create a newline
            print()
            print(counter, " ", end="")
        else:
            print(counter, " ", end="")


if __name__ == "__main__":
    main()
