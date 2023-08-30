from scheduler import runEverydayAt
from helper import contestToday
from helper import fetchContestFromDatabase
from alexa import triggerRoutine
import json

env = json.load(open("config.json", "r"))
announce_time = env["EVENT_TRIGGER_TIME"]


def runRoutineIfAvailable():
    contest_today = contestToday(fetchContestFromDatabase())
    if len(contest_today):
        print("Contest Available for today")
        print("Triggering Routine")
        triggerRoutine()


def routine_main():
    print("Starting Routine API\n")
    print("Routine will be triggered at: ", announce_time)
    runEverydayAt(announce_time, runRoutineIfAvailable)
