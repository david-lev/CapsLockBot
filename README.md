<img src="https://cdn.iconscout.com/icon/premium/png-512-thumb/capslock-3-617408.png" width="100" height="100">

# CapsLockBot Converter

### Telegram bot to convert capslock messages to their real language.

Everyone is probably familiar with the situation which a message is sent and finds that CapsLock mode was activated when typing and now the message appears in capital letters in English instead of the source language. The following bot solves this problem:
- Edit the 'capslock-message' and first type the bot user to go inline with the original message. Click on the window that will appear and you will receive the translated message.
- The bot is adapted for working in groups without the need to edit the message. Add the bot to the group with delted messages permission, replay to each 'CapsLock message' with the command `/caps` and the bot will respond with the converted message.

> You can check our bot [here](https://t.me/CapslockHEbot) (in Hebrew).

## configuration:
- Clone this reposetory:
```
git clone https://github.com/david-lev/CapsLockBot.git
```
- Install requirements (``pyrogram, tgcrypto``):
```
pip3 install -U pyrogram tgcrypto
```
- Edit and insert the folowing values into the [config](/config.ini) file:
```
[pyrogram]
api_id = XXXXXXXXXXX
api_hash = XXXXXXXXXXXXXXXXXXXXXXXXXX
bot_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

[telegram]
bot_username = YourBotUsername (Without @)
```
the ``api_id`` & ``api_hash`` You can get from [my.telegram.org](https://my.telegram.org).
``bot_token`` & ``bot_username`` you can get by create new bot on [BotFather](https://t.me/BotFather).
- Edit the [main.py](/main.py#L11) file and change the caps values for the compatibility of your keyboard buttons.
- Run the bot:
```
python3 main.py
```
---
![]()
Created with ❤️ by [David Lev](https://t.me/davidlev) & [Yehuda By](https://t.me/M100achuzBots)
