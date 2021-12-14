import random
import time

import requests as requests


def roll_dice():
    print("rolling..")
    return random.randint(1, 9)

def guess_number(num):
    if roll_dice() == num:
        return "you won"


def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']


def magic_number():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    return a+b


def silly():
    param = {
        "timestamp": time.time(),
        "number": random.randint(1, 9)
    }
    response = requests.get("https://httpbin.org/get", param)
    if response.status_code == 200:
        return response.json()['args']


guess_number(3)
origin = get_ip()
print(origin)

print(magic_number())

print(silly())
