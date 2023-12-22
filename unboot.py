import os
from boot import *
from pyrogram import *

try:
    with open(f"{DIR}OS_COUNT.txt", "r") as f:
        OS_COUNT = int(f.read())
except Exception as e:
    print("ERROR", e)

if OS_COUNT > 0:
    @bot.on_message(filters.command("unboot") & filters.user(OWNER_ID))
    def unboot (bot, message):
        # Currently Only Os Allowed To Boot So Unbooting
        bot.send_message(message.chat.id, "Unbooting OS")
        try:
            os.remove(f"{DIR}Os.txt")
            with open(f"{DIR}OS_COUNT.txt", "w") as g:
                OS_COUNT = int(g.write(0))
            bot.send_message(message.chat.id, "Successfully Unbooted Your Os")
            print("OS Unbooted")
            exit()
        except Exception as e:
            print("Somthing Went Wrong While Unbooting OS")
            print(e)
            exit()
else:
    print(None)
