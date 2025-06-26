# how to shield sensitive data (passwords, api keys, etc)
from getpass import getpass
import os

# 1. read from a file
OMDBAPI_API_KEY = open("EXAMPLES/omdbapikey.txt").read().rstrip()

# 2. read from keyboard
PASSWORD = getpass("Enter password: ")
print(f"My password is {PASSWORD}")

# 3. get from environment variable
PASSWORD = os.getenv("MYPASSWORD")
print(f"My password is {PASSWORD}")
