"""
This file contains all the helper functions used in the project

Functions:

    getAvailableContests: Returns the list of all the available contests from codeforces using codeforces API
    convertSecondsToTime: Converts the given seconds to hours, minutes and seconds
    prettyPrintContests: Prints the contests in a pretty format
    unixToDateTime: Converts the given unix time to date and time
    contestAlreadyExists: Checks if the contest already exists in the database or not
    uploadToDatabase: Uploads the available contests to the database
    fetchContestFromDatabase: Fetches all the contests from the database
    contestToday: Returns the list of contests that are taking place today
    is_past: Checks if the given time is in past or not
    deletePastContest: Deletes the past contests from the database


Author : @NotTheRightGuy
"""


import requests
import datetime
from Client import get_client

client = get_client()


def getAvailableContests():
    """
    Returns the list of all the available contests from codeforces using codeforces API

    Returns:
        list: list of all the available contests

    """
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    data = response.json()
    contests = data['result']
    availableContests = []
    for contest in contests:
        if contest['phase'] == 'BEFORE':
            availableContests.append(contest)
    return availableContests


def convertSecondsToTime(seconds):
    """
    Converts the given seconds to hours, minutes and seconds

    Args:
        seconds (int): time in seconds

    Returns:
        str: time in hours, minutes and seconds
    """
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours} hours {minutes} minutes {seconds} seconds"


def prettyPrintContests(contests):
    """
    Prints the contests in a pretty format

    Args:
        contests (list): list of contests
    """

    for contest in contests:
        print(f""" 
              
        ================================
        Contest ID: {contest["id"]}
        Contest Name: {contest["name"]}
        Duration : {convertSecondsToTime(contest["durationSeconds"])}
        Start Time: {unixToDateTime(contest["startTimeSeconds"])}
        ================================

        """)


def unixToDateTime(unixTime):
    """
    Converts the given unix time to date and time

    Args:
        unixTime (int): time in unix format

    Returns:
        str: time in date and time format
    """

    return datetime.datetime.fromtimestamp(unixTime).strftime('%Y-%m-%d %H:%M:%S')


def contestAlreadyExists(contestId):
    """
    Checks if the contest already exists in the database or not

    Args:
        contestId (int): contest id

    Returns:
        bool: True if contest already exists else False
    """
    data, count = client.table("Contests").select(
        "id").eq("id", str(contestId)).execute()
    return len(data[1]) != 0


def uploadToDatabase():
    """
    Uploads the available contests to the database
    """

    contests = getAvailableContests()
    for contest in contests:
        if not contestAlreadyExists(contest["id"]):
            data, count = client.table("Contests").insert({
                "id": contest["id"], "name": contest["name"], "duration": contest["durationSeconds"], "start_time": unixToDateTime(contest["startTimeSeconds"])}).execute()
            print("\nContest " + str(contest["id"]) + " added to database\n")


def fetchContestFromDatabase():
    """_
    Fetches all the contests from the database

    Returns:
        list: list of all the contests
    """
    data, count = client.table("Contests").select("*").execute()
    return data[1]


def contestToday(contests):
    """
    Returns the list of contests that are taking place today

    Args:
        contests (list): list of all the contests

    Returns:
        list: list of contests that are today
    """
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    contest_today = []
    for contest in contests:
        if contest["start_time"].split("T")[0] == today:
            contest_today.append(contest)
    return contest_today


def is_past(database_time_str):
    """
    Checks if the given time is in past or not

    Args:
        database_time_str (str): time in string format

    Returns:
        bool: True if the time is past else False
    """
    db_format = "%Y-%m-%dT%H:%M:%S"
    current_format = "%Y-%m-%d %H:%M:%S"
    db_time = datetime.datetime.strptime(database_time_str, db_format)
    current_time = datetime.datetime.strptime(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), current_format)
    return db_time < current_time


def deletePastContest():
    """
    Deletes the past contests from the database
    """
    data, count = client.table("Contests").select("*").execute()
    contests = data[1]
    for contest in contests:
        if is_past(contest["start_time"]):
            client.table("Contests").delete().eq("id", contest["id"]).execute()
            print(f"Contest {contest['id']} deleted from database")


def extractHourMinute(time_str):
    dt = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S')
    return f"{dt.hour}:{dt.minute}"


def to_12_hour_format(time_str):
    hour, minute = map(int, time_str.split(':'))

    if 0 <= hour < 12:
        am_pm = "AM"
        if hour == 0:
            hour = 12
    else:
        am_pm = "PM"
        if hour > 12:
            hour -= 12

    return f"{hour}:{minute:02} {am_pm}"
