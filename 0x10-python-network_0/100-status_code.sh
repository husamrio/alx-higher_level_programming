#!/bin/bash
# URL, display status code only Post Request
curl -sLIw '%{http_code}' "$1" -o /dev/null
