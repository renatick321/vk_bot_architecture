token = ''
confirmation_token = ''
url = ''
title = ""
secret_key = ""




from vkbottle import Bot
from vkbottle.callback import BotCallback
callback = BotCallback(
    url=url,
    title=title,
    secret_key=secret_key,
)
bot = Bot(token=token, callback=callback)
