import json
from scheduler import runEverydayAt
from alexa import sendToAlexa
from helper import deletePastContest
from helper import uploadToDatabase
from helper import extractHourMinute
from helper import to_12_hour_format
from helper import contestToday
from helper import fetchContestFromDatabase
import time
from helper import clearScreen

env = json.load(open("config.json", "r"))
announce_time = env["EVENT_TRIGGER_TIME"]
delete_time = env["DELETE_CONTEST_TIME"]
upload_time = env["UPLOAD_TO_DATABASE_TIME"]


def makeAnnouncement():
    contest_today = contestToday(fetchContestFromDatabase())
    for contest in contest_today:
        print("Sending Announcement for contest: ",
              contest["id"], " at ", contest["start_time"])
        time_of_contest = to_12_hour_format(
            extractHourMinute(contest["start_time"]))
        text_to_speak = "You have a codeforces contest today at {}. Make sure to register yourself and attempt it.".format(
            time_of_contest)
        sendToAlexa(text_to_speak)


def announcement_main():
    print("Starting Announcement API\n")
    print("Announcement will be made at: ", announce_time)
    runEverydayAt(delete_time, deletePastContest)
    runEverydayAt(upload_time, uploadToDatabase)
    runEverydayAt(announce_time, makeAnnouncement)
