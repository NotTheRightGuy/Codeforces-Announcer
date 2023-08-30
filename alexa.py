import requests
import json

env = json.load(open("config.json", "r"))
MONKEY_API = env["VOICEMONKEY_API"]
DEVICE_NAME = env["ALEXA_DEVICE_NAME"]
ROUTINE_NAME = env["ROUTINE_NAME"]


def sendToAlexa(text_to_send):
    text_to_insert = "%20".join(text_to_send.split(" "))
    url = f"https://api-v2.voicemonkey.io/announcement?token={MONKEY_API}&device={DEVICE_NAME}&text={text_to_insert}&voice=Raveena"
    requests.get(url)


def triggerRoutine():
    url = f"https://api-v2.voicemonkey.io/trigger?token=54c5ec103740051f04611a2e9448cd7b_63bb1d2a627d8f56f721beaab30448db&device={ROUTINE_NAME}"
    requests.get(url)
