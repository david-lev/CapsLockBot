from pyrogram import Client, filters, types
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
bot_username = config.items("telegram")[0][1]

app = Client("capslock")

#  convert capslock chars to your language (hebrew in this case):
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


#  replay filters
@app.on_message(filters.group & filters.reply & filters.command(["caps", f"caps@{bot_username}"]))
def main(_, msg: types.Message):
    gib_msg = msg.reply_to_message
    gib = gib_msg.text.lower()
    print(gib)
    new_str = str()

    #  replace capslock chars with your language:
    for char in gib:
        if caps.get(char):
            new_str += caps.get(char)

        else:
            new_str += char

    gib_msg.reply(new_str)

    #  delete the /caps command
    try:
        msg.delete()
    except:
        pass


#  welcome message
@app.on_message(filters.command("start") & filters.private)
def private(_, msg: types.Message):
    txt = "Hi! Add me to your group and give me permission to delete messages; Respond to any 'capslock' message with " \
          "the command `/caps`, and I will convert it into spoken language!\n\nThis bot " \
          "made with ❤️by [David-Lev](t.me/davidlev) && [Yeuda-By](t.me/m100achuzBots)."
    msg.reply(txt, disable_web_page_preview=True,
              reply_markup=types.InlineKeyboardMarkup([
                  [types.InlineKeyboardButton("➕ Add to your group ➕",
                                              url=f"http://t.me/{bot_username}?startgroup=true")]
              ]))


app.run()
