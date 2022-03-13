from handlers import bot
from flask import Flask, request, json
from config import confirmation_token, secret_key

app = Flask(__name__)

@app.route('/', methods=['POST'])
async def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data["secret"] == secret_key:
        await bot.process_event(data)
        return 'ok'

