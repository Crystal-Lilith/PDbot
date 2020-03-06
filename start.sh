#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
export TOKEN
export PREFIX
sudo gem install discordrb dotenv
while :
do
    ruby rbot.rb & python3 web/server.py & python3 dbot.py & python3 hbot.py
    killall python3 ruby
    git fetch
    git pull
done
