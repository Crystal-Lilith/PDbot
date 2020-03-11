import os
from flask import Flask, url_for, redirect, render_template
from flask_discord import DiscordOAuth2Session
from gevent.pywsgi import WSGIServer

app=Flask(__name__)

app.secret_key = b'Y\xd9\x8c\xcc\x8e\x16\x8d\x94\x93{/\xa2\x16\x88\t"\x11j\xc3/\xb9\xf9ra'

app.config["DISCORD_CLIENT_ID"] = os.environ.get('CLIENT_ID')
app.config["DISCORD_CLIENT_SECRET"] = os.environ.get('CLIENT_SECRET')
app.config["DISCORD_REDIRECT_URI"] = "https://pden.net/callback"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
discord = DiscordOAuth2Session(app)

def html_format(file):
    try:
        with open(file) as f:
            if file.lower().endswith(".css"):
                return f.read()
            try:
                return eval(f"f'''"+f.read().replace("{", "|~~").replace("}", "~~|").replace("$>", "{").replace("}", "<$")+"'''").replace("|~~", "{").replace("~~|", "}")
            except Exception as e: # Catching all errors so we can have this working no matter what
                print(e)
                return f.read()
    except FileNotFoundError:
        return "The page you were looking for could not be found, is it valid?", 404

@app.route('/')
def index():
    try:
        user = discord.fetch_user()
        login_status = discord.authorized
        return render_template('index.html', user=user, login_status=login_status)
    except FileNotFoundError:
        return "No index.html file"
    except:
        class user:
            name = 'Login'
        return render_template('index.html', user=user, login_status=False)

@app.route('/contact')
def contact():
    try:
        user = discord.fetch_user()
        login_status = discord.authorized
        return render_template('contact.html', user=user, login_status=login_status)
    except FileNotFoundError:
        return "No Contact.html file"
    except:
        class user:
            name = 'Login'
        return render_template('contact.html', user=user, login_status=False)

@app.route('/login')
def login():
    try:
        return discord.create_session()
    except:
        return redirect('/')

def logout():
    try:
        discord.revoke()
    except:
        pass

@app.route("/callback")
def callback():
    try:
        discord.callback()
        return redirect('/')
    except:
        return redirect('/')

@app.route("/commit", methods=['POST'])
def commit_update():
    os.system("bash stop.sh")
    return ''

# @app.route("/<path:filepath>")
# def page_loader(filepath):
#     return html_format("./"+filepath)

WSGIServer(('0.0.0.0', 8080), app).serve_forever()
