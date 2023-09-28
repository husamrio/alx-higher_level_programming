#!/bin/bash
# Options take in URL, display all methods accepted
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
