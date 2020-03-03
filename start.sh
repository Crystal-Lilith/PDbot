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
    ruby rbot.rb & python3 dbot.py & python3 hbot.py
    git fetch
    git pull
done
