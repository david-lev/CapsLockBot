from typing import Union
from pyrogram.types import Message, InlineQuery

# Here you can add your language strings. just add on every dict new key with your language code and insert the value.
# keep you're mind that languages are displayed accordingly to your client (app, software) lang.

strings = {
    "caps_private": {
        "en": "❌ This command is for group use only, in replay to a message.",
        "he": "❌ פקודה זו ניתנת לשימוש בקבוצות בהגבה על הודעה 'מקופסלקת' בלבד"
    },
    "start_msg": {
        "en": "Hi {}! 👋\n\n"
              "🤖 **This bot allows you to 'translate' messages sent when the keyboard was in CapsLock mode.**\n\n"
              "📖️️ Send /help for more information."
              "\n\n🎛 This bot made with ❤️by [David-Lev](t.me/davidlev) && [Yeuda-By](t.me/m100achuzBots).",
        "he": "היי {}! 👋\n\n"
              "🤖 **בוט זה מאפשר להמיר הודעות שנשלחו כשהמקלדת היתה על אנגלית או במצב קאפסלוק - לעברית.**\n\n"
              "📖️ למידע נוסף שלחו /help."
              "\n\n🎛 בוט זה נוצר על ידי [David-Lev](t.me/davidlev) && [Yeuda-By](t.me/m100achuzBots)."
    },
    "help_msg": {
        "en": "📖️️ **How to use:**\n\n"
              "--• Inline mode:--\nDid you send a 'CapsLock-message' in any chat? Edit it and add the bot user - `@{}` "
              "at the beginning of the message and add space between them, the bot will display an Inline message "
              "showing the 'translation', click on it to send the converted message.\n\n"
              "--• Groups:--\nYou can add me to your group and give me permission to delete messages. Replay to any "
              "'capslock' message with the `/caps` command and I'll convert it into spoken language!\n\n "
              "--• Private:--\nI also work in private, send or forward any message here and I will translate it into "
              "spoken language."
              "\n\nThis bot made with ❤ by [David-Lev](t.me/davidlev) && [Yeuda-By](t.me/m100achuzBots).",
        "he": "📖️️ **כיצד להשתמש בבוט?**\n\n"
              "--• מצב אינליין:--\nשלחתם הודעה מקופסלקת בכל צ'אט שהוא? ערכו את ההודעה והוסיפו את יוזר הבוט בתחילתה - "
              "`@{}`, השאירו רווח בין היוזר לבין ההודעה. הבוט יציג את 'התרגום' בחלונית אינליין ותוכלו ללחוץ על החלונית "
              "ולשלוח את ההודעה המתוקנת באותו הצ'אט.\n"
              "--• שימוש בקבוצות:--\nהוסיפו את הבוט לקבוצה ותנו לו הרשאה למחיקת הודעות. כעת הגיבו לכל הודעה "
              "'מקופסלקת' עם הפקודה `/caps` והבוט ימיר את ההודעה לעברית.\n"
              "--• צ'אט בבוט:--\nניתן לשלוח או לעביר הודעות ישירות אל הבוט ולקבל את תרגומן לעברית.\n\n"
              "🎛 רובוט זה נוצר על ידי [David-Lev](t.me/davidlev) && [Yeuda-By](t.me/m100achuzBots)."
    },
    "add_to_group": {
        "en": "Add to your group",
        "he": "הוסיפו אותי לקבוצה"
    },
    "inline_converter": {
        "en": "Converter",
        "he": "המר באינליין"
    },
    "source_code": {
        "en": "GitHub",
        "he": "גיטהאב"
    }
}


# Return message depend on the client language:
def lang_msg(msg_obj: Union[Message, InlineQuery], msg_to_rpl: str) -> Union[str, bool]:
    msg = strings.get(msg_to_rpl)

    if not msg:
        return False

    lang_client = msg_obj.from_user.language_code
    if msg.get(lang_client):
        return msg[lang_client]
    else:
        return msg["en"]
