require 'discordrb'
require 'dotenv'
require 'json'

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

cmds = []
for command in client.commands.keys
  cmds << command
end
File.write(File.join('cmds', 'rcmds.json'), cmds.to_json, mode: "w+")

client.run()