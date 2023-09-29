#!/usr/bin/python3
"""
usage: ./3-error_code.py http://0.0.0.0:5000/status_401
given URL & email as params, display response body utf-8, print error codes
*****
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
