from os import environ
import aiohttp
from pyrogram import Client, filters
import requests 
from pySmartDL import SmartDL
import shutil
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent

#from gofile2 import Async_Gofile
API_ID = 4568546
API_HASH = "07abc3db513a588ee4322eeb5f7b2433"
BOT_TOKEN = "5410101600:AAEf17Zm-axXngsTu5rW1oyKdNsPpFjusnY"
API_KEY = environ.get('API_KEY', '5fd20df0c4db85798dd4f5ff3d03e3606a94f98b')

bot = Client('gplinkt44ubodt',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(f"@lovetoride")
@bot.on_message(filters.media & filters.private )
async def link_handler(bot, message):
    file_caption = f"**{message.caption}**"
    tmp_directory_for_each_user = "downloads/"
    if not os.path.isdir(tmp_directory_for_each_user):
        os.makedirs(tmp_directory_for_each_user)
    await message.reply("<b>Download Started </b>") 
    tmp_directory_for_each_user = await bot.download_media(message, tmp_directory_for_each_user)
    file_name = os.path.basename(tmp_directory_for_each_user)
    path2 = f'downloads/{file_name}'
    lk =['@Team_HDT','@HEVC_Mob' , '@DevHEVC' ,'@NOob_Encoders','@NOoB_Encoders','@TamilMob_LinkZz','@DVDWOALL','@HDTalkies']
    for i in lk: 
        file_name = file_name.replace(i ,"@HEVC_Moviesz ")
        file_name = file_name
    file_name = file_name
    for i in lk: 
        file_caption = file_caption.replace(i ,"")
        file_caption = file_caption
    file_caption = file_caption
    print(file_caption)
    #file_name = file_name.replace("@HEVC_Moviesz","@Trvpn")
    
    path11 = f'downloads/{file_name}'
    path2 = os.rename(path2, path11)
    path11 = f'downloads/{file_name}'
    path = path11
    ids = message.chat.id
    await up1(path,ids,file_caption)
    
@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    link = f"{message.text}"
    ids = message.chat.id
    await message.reply("<b>Download Started<b>")    
    url = link
    await download(link,ids)
    
async def download(link,ids):
    url = link
    tmp_directory_for_each_user = "downloads/"
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
        
        na = f'file :{os.path.basename(path)}:Download Successful \n\nDownloaded File Size : {k}\n\n Download Completed :{k1} ..Uploading To Gofile.com..'
        ids = ids 
        await bot.send_message (ids ,na)
        
    except Exception as e:
        await bot.send_message (ids ,e)
   
    old_file_name =  os.path.basename(path)
    if old_file_name.startswith('www'):
        new_file_name = ' '.join(old_file_name.split()[2:])
        new_file_name = '@HEVC_Moviesz ' + new_file_name
        path1 = f'{tmp_directory_for_each_user}{new_file_name}'
        path = os.rename(path, path1)
        print(path)
        path = f'{tmp_directory_for_each_user}{new_file_name}'
        #await gofi(path,ids)
        await up(path,ids)
    else:
        ids = ids 
        path = path
        new_file_name = os.path.basename(path)
        new_file_name = '@HEVC_Moviesz ' + new_file_name
        path1 = f'{tmp_directory_for_each_user}{new_file_name}'
        print(path)
        
        path = os.rename(path, path1)
        path = f'{tmp_directory_for_each_user}{new_file_name}'
        #await gofi(path,ids)
        await up(path,ids)   
async def up(path,ids):
    ids =ids 
    await bot.send_message(ids,"Uploading To Telegram ")
    print('up to tg')
    path = path
    file_name =  os.path.basename(path)
    
    if file_name.startswith('www'):
        file_name = ' '.join(file_name.split()[2:])
    else:
        file_name = file_name
    print(file_name)

    file_name = f'<b>{file_name}  \n\nUploaded By: @HEVC_Moviesz\nJoin : ðŸ”— @Tamil_Links_Official ðŸ”—</b>'
    try:
        await bot.send_document(
                    chat_id=ids,
                    document=path,
                    thumb = "/home/lovetoride/gofile/photo_2022-06-09_20-20-39.jpg",
                    
                    caption=file_name,
                    parse_mode="HTML"
                    #F
                    )
        di = f'Cleaning Directory  :{path}'
        await bot.send_message(ids ,di)
        
        a = shutil.rmtree(path)
        
    except:
        pass
    try:
        b = os.remove(path)
        di = f'Cleaning Directory  :{path}'
        #await bot.send_message(ids ,di)
        
    except:
        pass
async def up1(path,file_caption):
    ids =ids 
    await bot.send_message(ids,"Uploading To Telegram ")
    print('up to tg')
    path = path
    file_name =  os.path.basename(path)
    
    if file_name.startswith('www'):
        file_name = ' '.join(file_name.split()[2:])
    else:
        file_name = file_name
    print(file_name)

    file_name = f'<b>{file_name}  \n\nUploaded By: @HEVC_Moviesz\nJoin : ðŸ”— @Tamil_Links_Official ðŸ”—</b>'
    try:
        await bot.send_document(
                    chat_id=ids,
                    document=path,
                    thumb = "/home/lovetoride/gofile/photo_2022-06-09_20-20-39.jpg",
                    
                    caption=file_caption,
                    parse_mode="HTML"
                    #F
                    )
        di = f'Cleaning Directory  :{path}'
        await bot.send_message(ids ,di)
        
        a = shutil.rmtree(path)
        
    except:
        pass
    try:
        b = os.remove(path)
        di = f'Cleaning Directory  :{path}'
        #await bot.send_message(ids ,di)
        
    except:
        pass



bot.run()
