import random
import string
import requests
import time
from clint.textui import colored
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("made by kramel")

def generate_random_string(length, include_numbers):
    letters = string.ascii_lowercase
    if include_numbers:
        letters += string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def check_username_availability(username):
    time.sleep(1)
    url = f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1337-04-20"
    response = requests.get(url)
    data = response.json()
    if 'message' in data and data['message'] == 'Username is valid':
        return True
    return False

def generate_roblox_username(length, include_numbers):
    while True:
        username = generate_random_string(length, include_numbers)
        available = check_username_availability(username)
        if available:
            print(colored.green(f"{username} is available!"))
            return username
        else:
            print((), end="\r")
            print(colored.red(f"{username} is unavailable!"), end="\r")

# Input for username length
username_length = int(input("How many characters? enter a number: "))

# Input for including numbers in the username
include_numbers_input = input("Include numbers in the username? (y/n): ")
include_numbers = include_numbers_input.lower() == 'y'
print()

# Input for number of usernames to generate
num_usernames = 9999999999999999999999999999

for _ in range(num_usernames):
    username = generate_roblox_username(username_length, include_numbers)

input("Press Enter to exit...")
