cmd = require '../../command.coffee'
ping = new cmd.Command(name: 'ping', -> message.reply('pong!'))
pong = new cmd.Command(name: 'pong', -> message.reply('ping!'))
module.exports = 
    { ping, pong }