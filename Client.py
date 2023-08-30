import os
from supabase import create_client, Client
import json

env = json.load(open("config.json", "r"))

url = env["SUPABASE_URL"]
key = env["SUPABASE_KEY"]


def get_client() -> Client:
    return create_client(url, key)
