from os import environ
import aiohttp
from pyrogram import Client, filters
import requests 
from pySmartDL import SmartDL
import shutil
import os

API_ID = 2054877
API_HASH = "4227c1e45e462209a3dcc67ada88a44f"
BOT_TOKEN = "5233615439:AAHSw5B4t5Q93uUexXxTrMDajl9FO7Yqilk"
API_KEY = environ.get('API_KEY', '5fd20df0c4db85798dd4f5ff3d03e3606a94f98b')

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**ððððð¢ð{message.chat.first_name}!**\n\n"
        "ð'ðº #ðOFILE ð¯ð¼ð. ðððð ðð²ð»ð± ðºð² ð¹ð¶ð»ð¸ ð®ð»ð± ð´ð²ð #GoFile ð¦ðµð¼ð¿ðð²ð»ð²ð± ð¨ð¥ð.Currently Support Direct Url\n\n ð§ðµð¶ð ðð¼ð ðð ð ð®ð±ð² ðð @lovetoride")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    link = f"{message.text}"
    

    url = link


    tmp_directory_for_each_user = "downloads"
    if not os.path.isdir(tmp_directory_for_each_user):
        os.makedirs(tmp_directory_for_each_user)
    dest = tmp_directory_for_each_user
    obj = SmartDL(url, dest)
    obj.start()
    path = obj.get_dest()
    print(path)
    k = obj.get_final_filesize(human=True)
    k1 = obj.get_dl_time(human=True)
    try:
        
        await message.reply(f'ð¥Download Successful \n\nðDownloaded File Size : {k}\n\n Download Completed :{k1} ..Uploading To Gofile.com..', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)
    files={"upload_file": open(path, "rb")}
    #file = {'file':open('Etharkkum Thunindhavan - Official Trailer  Suriya  Sun Pictures  Pandiraj  DImman.mp4',"rb")}
    url = 'https://store3.gofile.io/uploadfile'
    description = {'description' :"TRVPN",'tags' : '@trvpn'}
    r = requests.post(url,files= files)

    json_data = r.json()
    json_data = json_data['data']['downloadPage']
    file_name =  os.path.basename(path)
    print(json_data)

    directory = dest
    try:
        
        await message.reply(f'FileName : {file_name}\n\nDownload Link : {json_data}', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)

    try:
        shutil.rmtree(directory)
    except:
        pass
    try:
        os.remove(directory)
    except:
        pass





bot.run()
