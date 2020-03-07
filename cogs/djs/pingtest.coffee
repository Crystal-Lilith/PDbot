module.exports =
    name: 'ping'
    description: 'Find the ping of the bot.'
    required_roles: []
    required_perms: ['test']
    execute: (message, args) -> message.channel.send "Pong! Your ping is: #{client.ping} ms"