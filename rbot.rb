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

for cog in (Dir::entries(File.join('cogs', 'drb')) - %w(. .. $))
  require_relative File.join('cogs', 'drb', cog)
  eval("client.include!(Cogs_#{cog.capitalize::delete_suffix('.rb')})")
end

if YAML.load(File.read(File.join("config", "serverticketchans.yaml"))) == false
    serverticketchans = Hash.new
    File.write(File.join('config', 'serverticketchans.yaml'), YAML.dump(serverticketchans))  
else
    serverticketchans = YAML.load(File.read(File.join("config", "serverticketchans.yaml")))
end

client.command(:setticketingchannel, description: "Set the default ticketing channel for this server.||<#channelinserver>", required_permissions: [:manage_server]) do |event, chan|
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
client.command(:showticketingchannel, description: "Show the default ticketing channel for this server.||No arguments") do |event|
    event.respond("The ticketing channel is <##{(YAML.load(File.read(File.join('config', 'serverticketchans.yaml')))[event.server.id])}>")
end
client.command(:openticket, description: "Open a ticket.||$openticket <description goes here>") do |event, *desc|
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
cmds = {}
client.commands.each do |name, command|
	perms = command.attributes[:required_permissions].map {|x| x=x.to_s.gsub('_', ' ').split.map(&:capitalize).join(' ')}
  	roles = command.attributes[:required_roles].map { |x| x = (client.server(668000598221651975)).role(x).name if x.is_a? Integer }
	cmds[name.to_s] = {'desc' => (command.attributes[:description].split('||'))[0], 'syntax' => (command.attributes[:description].split('||'))[1], 'required_roles'=>roles, 'required_perms'=>perms}
end
dpycmds = JSON.parse(File.read(File.join('cmds', 'dcmds.json')))
File.write(File.join('cmds', 'rcmds.json'), cmds.to_json, mode: "w+")
client.command(:help, description: "A help command.||<cmdname> for help on specific command") do |event, cmdname|
	if cmdname == nil; break
	else
		cmdname.downcase!
		if cmds.member?(cmdname)
			event.send_embed do |e|
				e.title = "#{cmdname} (#{(cmds[cmdname])['syntax']})"
				e.description = "**Description:** #{(cmds[cmdname])['desc']}\n**Required roles:** #{((cmds[cmdname])['required_roles']).join(',')}\n**Required permissions:** #{((cmds[cmdname])['required_perms']).join(',')}"

				e.color = 0x0a7187
			end
		elsif dpycmds.member?(cmdname)
			event.send_embed do |e|
				e.title = "#{cmdname} (#{(dpycmds[cmdname])['syntax']})"
              	e.description = "**Description:** #{(dpycmds[cmdname])['desc']}"
				e.color = 0x0a7187
			end
		else
			event.send_embed do |e|
				e.title = "Error"
				e.description = "Command not found! Please make sure you spelled it right. See $help to see available commands."
				e.color = 0x7C0A02
			end
		end
	end
end
client.run()

