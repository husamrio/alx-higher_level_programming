#!/bin/bash
# Post Request take in URL, POST key:vals; Usage: ./5-post_params
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
