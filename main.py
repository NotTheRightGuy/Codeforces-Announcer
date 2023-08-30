"""
Author : NotTheRightGuy
"""
import os
import sys
import json
import time

env = json.load(open("config.json", "r"))


def checkIfAllGood():
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


def clearScreen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":
    checkPassed = checkIfAllGood()
    # clearScreen()
    print("How would you like to proceed?")
    print("Use Announcement API to announce the contest along with time")
    print("\n1. Announcement API")
    print("2. Routine API")
    print("3. Test Functionality of Announcement API")
    choice = input("\n>>> ")
