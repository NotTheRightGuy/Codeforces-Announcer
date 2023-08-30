"""
Author : NotTheRightGuy
"""

import sys
import json
import time
from announcement import announcement_main
from routine import routine_main
from announcement import makeAnnouncement
from routine import runRoutineIfAvailable
from helper import clearScreen
from scheduler import scheduler
from helper import uploadToDatabase


env = json.load(open("config.json", "r"))


def checkIfAllGood():
    print("Checking if all the variables in configs are set")
    count = 0
    for key, value in env.items():
        time.sleep(0.2)
        if value == "":
            print(key, "is not set")
            count += 1
            time.sleep(1)
        else:
            print(key, "Found!")
    return count == 0


def menu():
    check = checkIfAllGood()
    clearScreen()
    if check:
        print("How do you want to proceed?")
        print("1. Announcement API")
        print("2. Routine API")
        print("3. Populate Database with Contests (Useful for first time)")
        print("===== Below options will only announce if there are contest available today =====")
        print("4. Trigger Announcement to check if everything is working fine")
        print("5. Trigger Routine to check if everything is working fine")
        var_input = input("\n>>> ")
        return var_input
    else:
        return False


def main():
    while True:
        var_input = menu()
        if var_input == False:
            print("Please set all the variables in config.json")
            break
        if var_input == "1":
            clearScreen()
            announcement_main()
            scheduler()
        elif var_input == "2":
            clearScreen()
            routine_main()
            scheduler()
        elif var_input == "3":
            clearScreen()
            uploadToDatabase()
            print("Database Populated")
            time.sleep(2)
            clearScreen()
        elif var_input == "4":
            clearScreen()
            makeAnnouncement()
            print("\nYou will hear your alexa announce if everything is working fine")
            time.sleep(5)
            clearScreen()
        elif var_input == "5":
            clearScreen()
            runRoutineIfAvailable()
            print("You will hear your alexa announce if everything is working fine")
            time.sleep(5)
            clearScreen()
        else:
            print("Invalid Input")
            break
    sys.exit(0)


if __name__ == "__main__":
    main()
