require 'discordrb'
require 'dotenv'
require 'json'
require 'yaml'


Dotenv.load
client = Discordrb::Commands::CommandBot.new(prefix: ENV["PREFIX"], token: ENV["TOKEN"])
client.remove_command(:help)
client.command(:sys, required_roles: [673405620527038478]) do |event, *cmd|
	output = `#{cmd.join ' '}`
	if output.length >= 2000
		File.write("output.txt", output)
		event.send_file(File.open("output.txt", "r"), caption: "Output was too long (over 2000 characters). Uploading as a file:")
		File.delete("output.txt")
    nil
	else
		event.send_embed do |e|
			e.color = '4287f5'
			e.title = "Output:"
			e.description = "```\n#{output}\n```"
		end
	end
end
FileUtils.mkdir_p "config"
if YAML.load(File.read(File.join("config", "serverticketchans.yaml"))) == false
    serverticketchans = Hash.new
    File.write(File.join('config', 'serverticketchans.yaml'), YAML.dump(serverticketchans))  
else
    serverticketchans = YAML.load(File.read(File.join("config", "serverticketchans.yaml")))
end
client.command(:setticketingchannel) do |event, chan|
    chan = client.parse_mention(chan)
    if chan.class == Discordrb::Channel
        serverticketchans[event.server.id] = chan.id
        event.respond "Set ticketing channel to <##{serverticketchans[event.server.id]}> (#{serverticketchans[event.server.id]})!"
        File.delete(File.join 'config', "serverticketchans.yaml")
        File.write(File.join("config", "serverticketchans.yaml"), YAML.dump(serverticketchans))
    else    
        event.respond("Channel #{chan} is invalid! Please make sure it exists in this server.")
    end
    nil
end
client.command(:showticketingchannel) do |event|
    event.respond("The ticketing channel is <##{(YAML.load(File.read(File.join('config', 'serverticketchans.yaml')))[event.server.id])}>")
end
cmds = []
for command in client.commands.keys
  cmds << command
end
File.write(File.join('cmds', 'rcmds.json'), cmds.to_json, mode: "w+")
client.run()