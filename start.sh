#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
export TOKEN
export PREFIX
export CLIENT_ID
export CLIENT_SECRET
sudo gem install discordrb dotenv
while :
do
    ruby rbot.rb & python3 dbot.py & bash -c "exec -a PDBot-c coffee cbot.coffee"
    bash stop.sh
    git fetch; git pull
done
