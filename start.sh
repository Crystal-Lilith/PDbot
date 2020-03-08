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
    ruby rbot.rb & authbind --deep python3 web/server.py & python3 dbot.py & node_modules/coffeescript/bin/coffee cbot.coffee & python3 hbot.py
    killall python3 ruby node
    git fetch
    git pull
done
