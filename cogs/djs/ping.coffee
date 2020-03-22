module.exports =
    name: 'ping'
    description: 'Find the ping of the bot.'
    required_roles: []
    required_perms: []
    execute: (message, args) -> message.channel.send "Pong! Your ping is #{message.client.ws.ping} ms (rounded to #{Math.round message.client.ws.ping} ms)."