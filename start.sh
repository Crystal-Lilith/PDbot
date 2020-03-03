#!/bin/bash
clear
export GEM_HOME=./.gem
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
export TOKEN
export PREFIX
gem install discordrb dotenv
while :
do
    ruby rbot.rb &
    cd web && python3 server.py &
    cd ..
    python3 pbot.py
    git fetch
    git pull
done
