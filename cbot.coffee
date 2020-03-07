fs = require 'fs'
Discord = require 'discord.js'
config = require('dotenv').config()
path=require 'path'

client = new Discord.Client()
client.commands = new Discord.Collection()

for file in fs.readdirSync(path.join('.', 'cogs', 'djs')) 
  cmd = require "./cogs/djs/#{file}" 
  client.commands.set(cmd.name, cmd)

client.once 'ready', () -> console.log 'Ready!'

client.on 'message', (message) ->
  return unless message.content.startsWith(config.prefix) or not message.author.bot
  args = message.content.slice(config.prefix.length).split(" ")
  command = args.shift().toLowerCase()
  return unless client.commands.has(command)
  try 
    client.commands.get(command).execute(message, args)
  catch error
    if error.length <= (2000 - 60)
      message.channel.send("There was an error in executing that command. It was:\n```#{e}```")
    else
      message.channel.send("There was an error in executing that command, but it is too large to send. Please check your console.")
      console.error(error)

cmds = {}
for cmd in client.commands
  cmds[cmd.name] = {desc: cmd.description, required_roles: cmd.required_roles, required_perms: cmd.required_perms}
fs.writeFileSync(path.join('.', 'cmds', 'djscmds.json'), JSON.stringify(cmds), encoding: 'utf8')
client.login(process.env.TOKEN)
