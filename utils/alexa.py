import requests
import os
from dotenv import load_dotenv
load_dotenv()

MONKEY_API = os.getenv("VOICEMONKEY_API")


def sendToAlexa(text_to_send):
    text_to_insert = "%20".join(text_to_send.split(" "))
    url = f"https://api-v2.voicemonkey.io/announcement?token={MONKEY_API}&device=vm--echo-dot&text={text_to_insert}&voice=Raveena"
    requests.get(url)
