#!/bin/bash

source /Users/moonseongha/Documents/code/script/static.sh

ROOT_DIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
PORT=56300

echo "$ROOT_DIR"

nohup ngrok http ${PORT} &>/dev/null &

NGROK_PUBLIC_URL=""
while [ -z "$NGROK_PUBLIC_URL" ]; do
  NGROK_PUBLIC_URL=$(curl -s -X GET http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' &)
  sleep 1
done


source "$ROOT_DIR/venv/bin/activate"
nohup python app.py  > /dev/null &

msg "http://localhost:4040"
echo
msg "${NGROK_PUBLIC_URL}/slack/events"
echo
msg "https://api.slack.com/apps/A06HQBV86LV/interactive-messages"
msg "https://api.slack.com/apps/A06HQBV86LV/event-subscriptions"
