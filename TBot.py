import telebot
import variables as v

bot = telebot.TeleBot(v.TOKEN)
path = v.ChatIDPath
global ID


@bot.message_handler(commands=["help", "start"])
def send(message):
    bot.reply_to(message, "Bot initiated succesfully")
    chatID = message.chat.id
    with open(path, "w") as f:
        f.write(str(chatID))


def sendDoc(path):
    ID = getID()
    bot.send_document(ID, open(path))


def sendPhoto(path):
    ID = getID()
    bot.send_photo(ID, open(path, 'rb'))


def msg(key):
    ID = getID()
    bot.send_message(ID, key)


def getID():
    with open(path, "r") as f:
        ID = f.readline()
    return ID


# bot.polling()
