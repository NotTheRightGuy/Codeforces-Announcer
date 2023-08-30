import helper
import scheduler
import time
import alexa


def makeAnnouncement():
    contest_today = helper.contestToday(helper.fetchContestFromDatabase())
    for contest in contest_today:
        time_of_contest = helper.to_12_hour_format(
            helper.extractHourMinute(contest["start_time"]))
        text_to_speak = "You have a codeforces contest today at {}. Make sure to register yourself and attempt it.".format(
            time_of_contest)
        alexa.sendToAlexa(text_to_speak)


def main():
    # Check the codeforces API for available contests
    # and upload new contest to the database every day at 00:00
    scheduler.runEverydayAt("00:00", helper.deletePastContest())
    scheduler.runEverydayAt("06:00", helper.uploadToDatabase())
    scheduler.runEverydayAt("07:00", makeAnnouncement())
