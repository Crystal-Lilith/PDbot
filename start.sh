clear
export GEM_HOME=./.gem
gem install discordrb dotenv
while :
do
    ruby rbot.rb & python3 dbot.py & python3 hbot.py
    git fetch --all
    git reset --hard
    git pull https://gitlab.com/Gsbhasin84/zap.git
done
