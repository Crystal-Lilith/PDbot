from sanic import Sanic
from sanic import response
from aiofile import AIOFile

app=Sanic(__name__)

async def render_template(file):
    try:
        async with AIOFile("./templates/"+file, 'r') as f:
            x = await f.read()
            return f
    except FileNotFoundError as fnfe:
        raise fnfe
    except Exception as e:
        print(e)
        return response.text(str(e))

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
