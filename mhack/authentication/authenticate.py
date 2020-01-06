import requests, json


def verify_new_user(code_response):
    headers = {'Authorization':'token ' + code_response}
    response = requests.get('https://api.github.com/user/', headers=headers)
    print(response.text)
    