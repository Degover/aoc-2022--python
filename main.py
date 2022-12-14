from src.d01.solution import *
from src.d07.solution import *
from src.d10.solution import *
from src.d12.solution import *


def main():
    day = input("Wich day do you want the solution for? ")
    match day:
        case "1":
            solve_d1()
        case "7":
            solve_d7()
        case "10":
            solve_d10()
        case "12":
            solve_d12()
        case _:
            print("Day not solved yet")


if __name__ == "__main__":
    main()
