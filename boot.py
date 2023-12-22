import sys
import os
import asyncio
from pyrogram import Client, filters
from pyrogram import *
import time
import subprocess

try:
    DIR = f"{os.getcwd()}/"
    print("Running On ", DIR)
except Exception as l:
    print("ERROR", l)



a_id = "10187126" #Api ID
a_hash = "ff197c0d23d7fe54c89b44ed092c1752"
#Token For Boot Loader ↓
BOT_TOKEN = "6545010659:AAFNji-VogCaD64CmwtCPOSiX3glPKQ3iH4"
OWNER_ID = 5965055071
TOKEN = "6910428877:AAFIFbleAgAtf42tNQuty-gRbl4ybWIIPCQ"

bot = Client("Boot Loader", bot_token=BOT_TOKEN, api_id=a_id, api_hash=a_hash)

try:
    try:
        with open(f"{DIR}OS_COUNT.txt", "r") as f:
            OS_COUNT = int(f.read())
    except ValueError as e:
        print("Got A ValueError Trying To solve it")
        print("")
        time.sleep(5)
        os.remove(f"{DIR}OS_COUNT.txt")
        print("Success✅, Please Restart The Boot Loader")
except Exception as y:
    with open(f"{DIR}OS_COUNT.txt", "w") as f:
        f.write("0")
    with open(f"{DIR}OS_COUNT.txt", "r") as g:
        OS_COUNT = int(g.read())
    

def restart_program():
    python = sys.executable
    script = os.path.abspath(sys.argv[0])
    os.execl(python, python, script, *sys.argv[1:])

if OS_COUNT == 0:
    print("No Os Detected, Boot a Os")
    try:
        @bot.on_message(filters.command("boot") & filters.user(OWNER_ID))
        async def boot(bot, message):
            await message.reply_text("**Send a OS file to Continue✅**")
            
            @bot.on_message(filters.document & filters.user(OWNER_ID))
            async def receive_os_file(_, message):
                global os_file, os_counter
                await message.reply_text("Saving.....")
                try:
                    
                    os_file = f"{DIR}Os.txt"  # Replace with the actual absolute path
                    file_info = message.document
                    await message.download(file_name=os_file)
                    await message.reply_text("OS file Saved✅")
                    with open(f"{DIR}OS_COUNT.txt", "w") as f:
                        f.write("1")
                    with open(f"{DIR}OS_COUNT.txt", "r") as g:
                        OS_COUNT = int(g.read())
                    print("Done ✅")
                    await message.reply_text("**Please Backup Your OS File because If You Get Error Your Os file Will be Deleted So Backup It ✅ **")
                    restart_program()
                except Exception as e:
                    print("Error", e)
                    await message.reply_text(f"Error, `{e}`")
    except Exception as e:
        print("OOPS Something went Wrong During First Boot")
        print(e)
       
elif OS_COUNT == 1:
    try:
        @bot.on_message(filters.command("boot") & filters.user(OWNER_ID))
        def bootos(client, message):
            bot.send_message(OWNER_ID, f"**Starting ⚡**")
            
            with open(f"{DIR}Os.txt", "r") as kk:
                CODE = kk.read()
            
            exec(CODE)
            bot.send_message(chat_id=OWNER_ID, text="** Your OS Has been Stopped **")
            print("Exited...")
            exit()
            sys.exit()
    except FileNotFoundError:
        print("Error, Os.txt Not Found Trying to Solve It")
        os.remove(f"{DIR}OS_COUNT.txt")
        print("Success, Please Restart The Program")
        exit()
    except Exception as e:
        print("ERROR, ", e)
        exit()
    

else:
    print("Something Went Wrong, Checking Errors....")
    time.sleep(3)
    try:
        if OS_COUNT > 1:
            print("ERROR, OS_COUNT is Above 1 So You Got this Error.")
            time.sleep(2)
            print(" ")
            print("Solving Error, This May take Few Moments")
            time.sleep(3)
            os.remove(f"{DIR}OS_COUNT.txt")
            print("Success")
            print("Error Solved Restart The Code")
            exit()
        elif OS_COUNT < 0:
            print("ERROR, OS_COUNT is Below 0 So You Got this Error.")
            time.sleep(2)
            print(" ")
            print("Solving Error, This May take Few Moments")
            time.sleep(3)
            os.remove(f"{DIR}OS_COUNT.txt")
            print("Success")
            print("Error Solved, Please Restart The Code")
            exit()
    except Exception as e:
        print("ERROR:", e)

try:
    with open(f"{DIR}OS_COUNT.txt", "r") as f:
        OS_COUNT = int(f.read())
except Exception as e:
    print("ERROR", e)

if OS_COUNT == 1:
    @bot.on_message(filters.command("unboot") & filters.user(OWNER_ID))
    def unboot (bot, message):
        # Currently Only Os Allowed To Boot So Unbooting
        bot.send_message(message.chat.id, "Unbooting OS")
        try:
            os.remove(f"{DIR}Os.txt")
            with open(f"{DIR}OS_COUNT.txt", "w") as g:
                g.write("0")
            bot.send_message(message.chat.id, "**Successfully Unbooted Your Os ✅**")
            print("OS Unbooted")
            restart_program()
        except Exception as e:
            print("Somthing Went Wrong While Unbooting OS")
            print(e)
            exit()
else:
    None

bot.run()
