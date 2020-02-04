from hata import Embed, eventlist, enter_executor
import requests, json

commands = eventlist()

@commands
async def meme(client, message):
    try:
        with open('./config/hata/meme.json') as f:
            data=json.load(f)
            thing = data['title'] + " - r/" + data['subreddit'] # oh lol
        embed=Embed(thing).add_image(data['url'])
        await client.message_create(message.channel,embed=embed)

        with open('./config/hata/meme.json', 'w+') as f:
            async with enter_executor():
                r=requests.get('https://meme-api.herokuapp.com/gimme')
                json.dump(json.loads(r.text), f)
    except Exception as e:
        print(e)
        async with enter_executor():
            r = requests.get('https://meme-api.herokuapp.com/gimme')
            with open('./config/hata/meme.json', 'w+') as f:
                json.dump(json.loads(r.text), f)