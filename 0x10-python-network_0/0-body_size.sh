#!/bin/bash
# Size of content-length print curl content size
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2