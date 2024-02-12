#!/bin/bash

source /Users/moonseongha/Documents/code/script/static.sh

cmd \
  "pkill -f app.py" \
  "stop slack-bot server"

cmd \
  "pkill ngrok" \
  "stop ngrok"
