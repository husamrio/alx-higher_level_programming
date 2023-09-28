#!/bin/bash
# Send header Take in URL, add header variable, displays "X-School!"
curl -sH "X-School-User-Id:98" "$1"
