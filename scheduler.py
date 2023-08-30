import time
import schedule


def runEverydayAt(time, func):
    """
    Runs the given function at the given time everyday

    Args:
        time (str): time in 24 hour format
        func (function): function to be executed
    """
    schedule.every().day.at(time).do(func)


def scheduler():
    """
    Runs the scheduler
    """
    while True:
        schedule.run_pending()
        time.sleep(1)
