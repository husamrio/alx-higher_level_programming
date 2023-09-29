#!/usr/bin/python3
"""
usage: ./8-json_api.py [letter only]
*****
given letter as param, POST to http://0.0.0.0:5000/search_user
*****
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    r = requests.post(url, data=payload)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
