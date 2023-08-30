import requests


def getAvailableContests():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    data = response.json()
    contests = data['result']
    availableContests = []
    for contest in contests:
        if contest['phase'] == 'BEFORE':
            availableContests.append(contest)
    return availableContests
