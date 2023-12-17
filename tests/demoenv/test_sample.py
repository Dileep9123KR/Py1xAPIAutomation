from dotenv import load_dotenv
import os
def test_suth():
    # username = "admin"
    # password = "password123"
    # directly giving username and passed within the code(hard-coded) is not a good way to implement
    # so we use another lib for overcome such scenarios
    # pip install python-dotenv
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username,password)
    # please note that, we don't push the .env file to github
