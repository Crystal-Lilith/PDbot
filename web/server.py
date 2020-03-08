from sanic import Sanic
from sanic import response
from aiofile import AIOFile
from os import listdir

app=Sanic(__name__)

async def render_template(file):
    try:
        async with AIOFile(f'web/templates/{file}', 'r') as f:
            x=await f.read()
            return response.html(str(x))
    except FileNotFoundError as fnfe:
        raise fnfe
    except Exception as e:
        print(e)
        return response.text(str(e))

app.static('/static', './static')
for filename in listdir('./static'):
    app.url_for('static', filename=filename) == f'/static/{filename}'

@app.route('/')
async def index(req):
    try:
        x = await render_template('index.html')
        return x
    except FileNotFoundError:
        return response.text("No index.html file")

@app.route('/contact')
async def contact(req):
    try:
        x = await render_template('contact.html')
        return x
    except FileNotFoundError:
        return response.text("No Contact.html file")
    
@app.route('/dashboard')
async def dashboard(req):
    try:
        x = await render_template('dashboard.html')
        return x
    except FileNotFoundError:
        return response.text("No dashboard.html file")

app.run('0.0.0.0', 8080, ssl={'cert': "keys/certificate.crt", 'key': "keys/private.key"})
