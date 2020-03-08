fs = require 'fs'
Discord = require 'discord.js'
require('dotenv').config()
path=require 'path'

client = new Discord.Client()
client.commands = new Discord.Collection()

for file in fs.readdirSync(path.join('.', 'cogs', 'djs')) 
  cmd = require "./cogs/djs/#{file}" 
  client.commands.set(cmd.name, cmd)

client.once 'ready', () -> console.log 'Ready!'

client.on 'message', (message) ->
  return unless message.content.startsWith(process.env.PREFIX) or not message.author.bot
  args = message.content.slice(process.env.PREFIX.length).split(" ")
  command = args.shift().toLowerCase()
  return unless client.commands.has(command)
  try
    hasperms = client.commands.get(command).required_perms.some((perm) -> message.member.guild.me.hasPermission(perm))
    message.reply hasperms
    
    if client.commands.get(command).required_perms is [] or hasperms is true
      client.commands.get(command).execute(message, args) 
    else
      message.reply("You don't have the required permissions to run this command.")
    
  catch error
    if error.length <= (2000 - 60)
      message.channel.send("There was an error in executing that command. It was:\n```#{e}```")
    else
      message.channel.send("There was an error in executing that command, but it is too large to send. Please check your console.")
      console.error(error)

cmds = {}
client.commands.forEach( (cmd)  =>
  cmds[cmd.name] = {desc: cmd.description, required_roles: cmd.required_roles, required_perms: cmd.required_perms}
)
fs.writeFileSync(path.join('.', 'cmds', 'djscmds.json'), JSON.stringify(cmds), encoding: 'utf8')
client.login(process.env.TOKEN)
