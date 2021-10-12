#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def degrees():
    integer = input("Enter a temperature (°C): ")
    try:
        number = float(integer)
        answer = (9 / 5) * number + 32
        print("{0}°C is equal to {1}°F".format(number, answer))

    except Exception:
        print("This was not a number")
    finally:
        print("")
        print("Done.")


def main():
    degrees()


if __name__ == "__main__":
    main()
