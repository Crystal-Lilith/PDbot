#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
sudo gem install discordrb dotenv
while :
do
    python3 dbot.py & ruby rbot.rb & bash -c "exec -a PDBot-c ./node_modules/coffeescript/bin/coffee cbot.coffee"
    bash stop.sh
    git fetch; git pull
done
