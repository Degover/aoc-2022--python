from src.d01.solution import *


def main():
    day = input("Wich day do you want the solution for? ")
    match day:
        case "1":
            solve_d1()
        case _:
            print("Day not solved yet")


if __name__ == "__main__":
    main()
