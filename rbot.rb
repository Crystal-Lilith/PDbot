require 'discordrb'
require 'dotenv'
require 'json'
require 'yaml'
require 'fileutils'
FileUtils.mkdir_p "config"
FileUtils.touch(File.join("config", "serverticketchans.yaml"))
FileUtils.touch(File.join("config", "latestticket.cfg"))
FileUtils.touch(File.join("config", "tickets.yaml"))
Dotenv.load
client = Discordrb::Commands::CommandBot.new(prefix: ENV["PREFIX"], token: ENV["TOKEN"])
client.command(:sys, required_roles: [673405620527038478], description: "Run a system command.") do |event, *cmd|
	output = `#{cmd.join ' '}`
	if output.length >= 2000
		File.write("output.txt", output)
		event.send_file(File.open("output.txt", "r"), caption: "Output was too long (over 2000 characters). Uploading as a file:")
		File.delete("output.txt")
    nil
	else
		event.send_embed do |e|
			e.color = 0x4287f5
			e.title = "Output:"
			e.description = "```\n#{output}\n```"
		end
	end
end


if YAML.load(File.read(File.join("config", "serverticketchans.yaml"))) == false
    serverticketchans = Hash.new
    File.write(File.join('config', 'serverticketchans.yaml'), YAML.dump(serverticketchans))  
else
    serverticketchans = YAML.load(File.read(File.join("config", "serverticketchans.yaml")))
end
client.command(:setticketingchannel, description: "Set the default ticketing channel for this server.") do |event, chan|
	if !event.author.role?(673405620527038478)  && !event.author.permission?(:manage_server)
		event.respond "You do not have permission to set the ticket channel!"
		break
	else;
	end
    chan = client.parse_mention(chan)
    if chan.class == Discordrb::Channel
        serverticketchans[event.server.id] = chan.id
        event.respond "Set ticketing channel to <##{serverticketchans[event.server.id]}> (#{serverticketchans[event.server.id]})!"
        File.delete(File.join 'config', "serverticketchans.yaml")
        File.write(File.join("config", "serverticketchans.yaml"), YAML.dump(serverticketchans))
    else    
		event.respond("Channel #{chan} is invalid! Please make sure it exists in this server.")
		nil
    end
end
client.command(:showticketingchannel, description: "Show the default ticketing channel for this server.") do |event|
    event.respond("The ticketing channel is <##{(YAML.load(File.read(File.join('config', 'serverticketchans.yaml')))[event.server.id])}>")
end
client.command(:openticket, description: "Open a ticket.") do |event, *desc|
	desc = desc.join(" ")
	ticketnumber = (File.read(File.join('config', 'latestticket.cfg')).to_i) + 1
	File.write(File.join('config', 'latestticket.cfg'), ticketnumber, mode: 'w+')
	File.write(File.join('config', 'tickets.yaml'), YAML.dump({ticketnumber=>{'author'=>event.author.id, 'desc'=>desc, 'opened'=>false}}), mode: 'a')
	event.send_embed do |e|
		e.color = 0x00FF00
		e.title = "Opened ##{ticketnumber}!"
		e.description = "**Author: #{event.author.mention}**\n#{desc}"
	end
end
cmds = Hash.new
client.commands.each do |name, command|
	cmds[name.to_s] = {'desc' => command.attributes[:description], 'perms' => [], 'roles' => []}
end
dpycmds = JSON.parse(File.read(File.join('cmds', 'dcmds.json')))
File.write(File.join('cmds', 'rcmds.json'), cmds.to_json, mode: "w+")
client.command(:help, description: "A help command.") do |event, cmdname|
	if cmdname == nil; break
	else
		cmdname.downcase!
		puts dpycmds.class, cmds.class
		if cmds.key?(cmdname) 
			event.respond("#{cmdname} | #{(cmds[cmdname])['desc']}\nRequired roles: #{(cmds[cmdname])['roles'].join ', '}\nRequired permissions: #{cmds[cmdname]['perms'].join ', '}")
		elsif dpycmds.key?(cmdname)
			event.respond("#{cmdname} | #{dpycmds[cmdname]['desc']}\nRequired roles: #{dpycmds[cmdname]['roles'].join ', '}\nRequired permissions: #{dpycmds[cmdname]['perms'].join ', '}")
		else
			event.respond("#{cmdname} isn't a valid command!")
		end
	end
end
client.run()

