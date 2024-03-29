#!/usr/bin/python3
"""
usage: ./5-hbtn_header https://intranet.hbtn.io
given URL as parameter, fetch URL and display value from reponse header
*****
"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
