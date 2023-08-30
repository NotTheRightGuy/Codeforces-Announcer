from utils.convertSecondsToTime import convertSecondsToTime
from utils.unixToDateTime import unixToDateTime


def prettyPrintContests(contests):
    for contest in contests:
        print(f""" 
              
        ================================
        Contest ID: {contest["id"]}
        Contest Name: {contest["name"]}
        Duration : {convertSecondsToTime(contest["durationSeconds"])}
        Start Time: {unixToDateTime(contest["startTimeSeconds"])}
        ================================

        """)
