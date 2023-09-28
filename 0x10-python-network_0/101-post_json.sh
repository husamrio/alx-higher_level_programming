#!/bin/bash
# Filename and URL, post contents of file Post Request
curl -sLX POST -H 'Content-Type: application/json' -d @"$2" "$1"
