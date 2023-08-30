from contestScrapper import getAvailableContests
from supabaseClient import get_client
import unixToDateTime


client = get_client()


def contestAlreadyExists(contestId):
    data, count = client.table("Contests").select(
        "id").eq("id", str(contestId)).execute()
    return len(data[1]) != 0


def uploadToDatabase():
    contests = getAvailableContests()
    for contest in contests:
        if not contestAlreadyExists(contest["id"]):
            data, count = client.table("Contests").insert({
                "id": contest["id"], "name": contest["name"], "duration": contest["durationSeconds"], "start_time": unixToDateTime.unixToDateTime(contest["startTimeSeconds"])}).execute()
