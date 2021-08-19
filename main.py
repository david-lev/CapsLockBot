import json

from pyrogram import Client, filters, types
import configparser
from strings import lang_msg, caps

config = configparser.ConfigParser()
config.read('config.ini')
bot_username = config.get("telegram", "bot_username")

app = Client("capslock")


# Convert function
def convert(caps_str: str) -> str:
    new_str = str()
    #  replace capslock chars with your language:
    for char in caps_str.lower():
        if caps.get(char):
            new_str += caps.get(char)
        else:
            new_str += char
    return new_str


# Save users id's
def save_user(uid: int, save_use: bool = True):
    """ save user/chat id to DB """
    if save_use:
        save_uses()
    ids_file = "users.json"
    try:
        with open(ids_file, "r") as oFile:
            users: list = json.load(oFile)
    except FileNotFoundError:
        users = []

    if uid not in users:
        users.append(uid)

    with open(ids_file, "w") as nFile:
        json.dump(users, nFile, indent=4)


# Save number of uses in the converter
def save_uses():
    """ save count of uses to DB """
    uses_file = "uses.txt"
    try:
        with open(uses_file) as usesO:
            uses = int(usesO.read())
    except FileNotFoundError:
        with open(uses_file, "w") as usesO:
            usesO.write("0")
        with open(uses_file) as usesO:
            uses = int(usesO.read())
    uses += 1
    with open(uses_file, "w") as usesO:
        usesO.write(str(uses))


# Convert caps messages inside groups
@app.on_message(filters.group & filters.reply & filters.command(["caps", f"caps@{bot_username}"]))
def main(_, msg: types.Message):
    msg.reply(convert(msg.reply_to_message.text))
    save_user(msg.from_user.id)
    #  delete the /caps command
    try:
        msg.delete()
    except:
        pass


# The caps command in private chats
@app.on_message(filters.private & filters.command("caps"))
def private(_, msg: types.Message):
    msg.reply(lang_msg(msg, "caps_private"))
    save_user(msg.from_user.id)


# Convert caps messages in private chats
@app.on_message(filters.private & ~filters.command(["start", "caps", "help"]))
def private(_, msg: types.Message):
    msg.reply(convert(msg.text))
    save_user(msg.from_user.id)


# Convert caps messages with inline mode
@app.on_inline_query()
def inline(_, query: types.InlineQuery):
    if not query.query:
        return
    query.answer([
        types.InlineQueryResultArticle(
            "🔠 CapsLockBot 🔠",
            types.InputTextMessageContent(convert(query.query)),
            description=convert(query.query),
            thumb_url="https://telegra.ph/file/a9fe802983616d6e82db3.png")
    ])
    save_user(query.from_user.id)


# Start and help messages
@app.on_message(filters.command(["start", "help"]) & filters.private)
def messages(_, msg: types.Message):
    if msg.command == ["start"]:
        msg.reply(lang_msg(msg, "start_msg").format(msg.from_user.mention), disable_web_page_preview=True,
                  reply_markup=types.InlineKeyboardMarkup([
                      [types.InlineKeyboardButton(f"🔠 {lang_msg(msg, 'inline_converter')} 🔠",
                                                  switch_inline_query_current_chat="RUCUYRHE")],
                      [types.InlineKeyboardButton(f"➕ {lang_msg(msg, 'add_to_group')} ➕",
                                                  url=f"https://t.me/{bot_username}?startgroup=true")],
                      [types.InlineKeyboardButton(f"🛠 {lang_msg(msg, 'source_code')} 🛠",
                                                  url="https://github.com/david-lev/CapsLockBot")]
                  ]))
    elif msg.command == ["help"]:
        msg.reply(lang_msg(msg, "help_msg").format(bot_username), disable_web_page_preview=True,
                  reply_markup=types.InlineKeyboardMarkup([
                      [types.InlineKeyboardButton(f"🔠 {lang_msg(msg, 'inline_converter')} 🔠",
                                                  switch_inline_query_current_chat="RUCUYRHE")],
                      [types.InlineKeyboardButton(f"➕ {lang_msg(msg, 'add_to_group')} ➕",
                                                  url=f"https://t.me/{bot_username}?startgroup=true")],
                      [types.InlineKeyboardButton(f"🛠 {lang_msg(msg, 'source_code')} 🛠",
                                                  url="https://github.com/david-lev/CapsLockBot")]
                  ]))
    save_user(msg.from_user.id, False)


app.run()
