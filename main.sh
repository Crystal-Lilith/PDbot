clear
export GEM_HOME=./.gem
gem install discordrb dotenv
bash -c "exec -a drbbot ruby rbot.rb" & bash -c "exec -a dpybot python3 dbot.py" & python3 hbot.py