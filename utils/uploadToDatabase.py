from contestScrapper import getAvailableContests
from supabaseClient import get_client

client = get_client()
contests = getAvailableContests()

for contest in contests:
    data, count = client.table("Contests").insert({
        "id": contest["id"], "name": contest["name"], "duration": contest["durationSeconds"], "start_time": contest["startTimeSeconds"]}).execute()
