import sys
import os
import asyncio
from pyrogram import Client, filters
from pyrogram import *
import time
import subprocess

try:
    DIR = f"{os.getcwd()}/"
    print("Running Directory Is", DIR)
except Exception as l:
    print("ERROR", l)

version = 0.51
a_id = "10187126" #Api ID
a_hash = "ff197c0d23d7fe54c89b44ed092c1752"
BOT_TOKEN = "6545010659:AAFNji-VogCaD64CmwtCPOSiX3glPKQ3iH4"
OWNER_ID = [5965055071, 2043144248]

system = Client("System", bot_token=BOT_TOKEN, api_id=a_id, api_hash=a_hash)
bot = system
system.start()
try:
    try:
        with open(f"{DIR}OS_COUNT.txt", "r") as f:
            OS_COUNT = int(f.read())
    except ValueError as e:
        time.sleep(5)
        os.remove(f"{DIR}OS_COUNT.txt")
        exit()
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
    print("Operating systems Not Detected, Install Manually")
    try:
        @system.on_message(filters.command("boot") & filters.user(OWNER_ID))
        async def boot(system, message):
            await message.reply_text("**Send a OS file to Continue ✅**")
            
            @system.on_message(filters.document & filters.user(OWNER_ID))
            async def receive_os_file(_, message):
                global os_file, os_counter
                SAVEFILE = await message.reply_text("**Saving Your File...**")
                try:
                    
                    os_file = f"{DIR}Os.txt"
                    file_info = message.document
                    await message.download(file_name=os_file)
                    await message.reply_text("**OS file Saved ✅**")
                    with open(f"{DIR}OS_COUNT.txt", "w") as f:
                        f.write("1")
                    with open(f"{DIR}OS_COUNT.txt", "r") as g:
                        OS_COUNT = int(g.read())
                    print("Saved Os File ✅")
                    await message.reply_text("**Please Backup Your OS File because If You Get Error Your Os file Will be Deleted So Backup It ✅ **")
                    await SAVEFILE.delete()
                    restart_program()
                except Exception as e:
                    print("Error", e)
                    await message.reply_text(f"Error, `{e}`")
    except Exception as e:
        print("OOPS Something went Wrong During First Boot")
        print(e)
        exit()
       
elif OS_COUNT == 1:
    try:
        bot.send_message(OWNER_ID, f"**Starting Your Os⚡**")
        with open(f"{DIR}Os.txt", "r") as kk:
            CODE = kk.read()
        exec(CODE)
    except FileNotFoundError: #ErrorHandling
        os.remove(f"{DIR}OS_COUNT.txt")
        restart_program()
    except Exception as e:
        print("ERROR, ", e)
        exit()
    

else:
    print("Something Went Wrong, Checking Errors....")
    time.sleep(3)
    try:
        if OS_COUNT > 1:
            print("error found, solving error..")
            time.sleep(2)
            print(" ")
            print(" ")
            time.sleep(1.5)
            os.remove(f"{DIR}OS_COUNT.txt")
            print("Success")
            restart_program()
        elif OS_COUNT < 0:
            print("error found, solving error..")
            time.sleep(2)
            print(" ")
            time.sleep(1.5)
            os.remove(f"{DIR}OS_COUNT.txt")
            print("Success")
            restart_program()
    except Exception as e:
        print("ERROR:", e)

try:
    with open(f"{DIR}OS_COUNT.txt", "r") as f:
        OS_COUNT = int(f.read())
except Exception as e:
    print("ERROR", e)

if OS_COUNT == 1:
    @system.on_message(filters.command("unboot") & filters.user(OWNER_ID))
    def unboot (system, message):
        # Currently Only Os Allowed To Boot So Unbooting
        Unbo = system.send_message(message.chat.id, "Unbooting OS")
        message.reply_document(f"{DIR}Os.txt", caption="**Maybe if You Wrongly ❌ Use this Command So I give Your File 🗃️**")
        try:
            os.remove(f"{DIR}Os.txt")
            with open(f"{DIR}OS_COUNT.txt", "w") as g:
                g.write("0")
            Unbo.delete()
            system.send_message(message.chat.id, "**Successfully Unbooted Your Os ✅**")
            print("Os Unbooted")
            restart_program()
        except Exception as e:
            print("Somthing Went Wrong While Unbooting OS")
            print(e)
            exit()

@system.on_message(filters.command("help") & filters.user(OWNER_ID))
def help (system, message):
    system.send_message(message.chat.id, """
**📚 Help 📚

Use /version To Get Bios Version
Use /shutdown For Force Shutdown
Use /restart For Force Restart
Use /boot Boot a Os
Use /unboot Delete A Booted Os file**
    """)
                     
@system.on_message(filters.command("version") & filters.user(OWNER_ID))
def biosversion (system, message):
    message.reply_text(f"**Your Current Bios Version is {version}**")

def shutdown():
    try:
        exit()
    except Exception:
        try:
            bot.stop()
        except Exception:
            sys.exit()
            
@system.on_message(filters.command("shutdown") & filters.user(OWNER_ID))
def stop (system, message):
    message.reply_text("**Shuting Down...**")
    shutdown()
    
@system.on_message(filters.command("restart") & filters.user(OWNER_ID))
def restartbot (system, message):
    message.reply_text("**Restarting...**")
    restart_program()

idle()   
system.stop()
