from pyrogram import Client, filters, types
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
bot_username = config.get("telegram", "bot_username")

app = Client("capslock")

# convert capslock chars to your language (hebrew in this case):
caps = {
    "q": "/",
    "w": "'",
    "e": "ק",
    "r": "ר",
    "t": "א",
    "y": "ט",
    "u": "ו",
    "i": "ן",
    "o": "ם",
    "p": "פ",
    "a": "ש",
    "s": "ד",
    "d": "ג",
    "f": "כ",
    "g": "ע",
    "h": "י",
    "j": "ח",
    "k": "ל",
    "l": "ך",
    "z": "ז",
    "x": "ס",
    "c": "ב",
    "v": "ה",
    "b": "נ",
    "n": "מ",
    "m": "צ",
    ",": "ת",
    ".": "ץ",
    "/": ".",
    ";": "ף",
    "'": ",",
    ")": "(",
    "(": ")"
}


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


# Convert caps messages inside groups
@app.on_message(filters.group & filters.reply & filters.command(["caps", f"caps@{bot_username}"]))
def main(_, msg: types.Message):
    msg.reply(convert(msg.reply_to_message.text))
    #  delete the /caps command
    try:
        msg.delete()
    except:
        pass


# The caps command in private chats
@app.on_message(filters.private & filters.command("caps"))
def private(_, msg: types.Message):
    msg.reply("This command is for group use only, in replay to a message.")


# Convert caps messages in private chats
@app.on_message(filters.private & ~filters.command(["start", "caps"]))
def private(_, msg: types.Message):
    msg.reply(convert(msg.text))


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


# Welcome message
@app.on_message(filters.command("start") & filters.private)
def start(_, msg: types.Message):
    txt = "Hi! Add me to your group and give me permission to delete messages; Respond to any 'capslock' message with " \
          "the command `/caps`, and I will convert it into spoken language!\n\nThis bot " \
          "made with ❤️by [David-Lev](t.me/davidlev) && [Yeuda-By](t.me/m100achuzBots)."
    msg.reply(txt, disable_web_page_preview=True,
              reply_markup=types.InlineKeyboardMarkup([
                  [types.InlineKeyboardButton("➕ Add to your group ➕",
                                              url=f"http://t.me/{bot_username}?startgroup=true")],
                  [types.InlineKeyboardButton("🔠 Converter 🔠", switch_inline_query_current_chat="RUCUYRHE")]
              ]))


app.run()
