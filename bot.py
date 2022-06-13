from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
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
        f"**𝗛𝗘𝗟𝗟𝗢🎈{message.chat.first_name}!**\n\n"
        "𝗜'𝗺 𝗚𝗣𝗹𝗶𝗻𝗸 𝗯𝗼𝘁. 𝗝𝘂𝘀𝘁 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗹𝗶𝗻𝗸 𝗮𝗻𝗱 𝗴𝗲𝘁 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗱 𝗨𝗥𝗟. \n\n 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗕𝘆 @CyberBoyAyush💖")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    link = f"{message.text}"
    try:
        shutil.rmtree('downloads')
    except:
        pass

    url = link


    tmp_directory_for_each_user = "downloads"
    if not os.path.isdir(tmp_directory_for_each_user):
        os.makedirs(tmp_directory_for_each_user)
    dest = tmp_directory_for_each_user
    obj = SmartDL(url, dest)
    obj.start()
    path = obj.get_dest()
    print(path)
    files={"upload_file": open(path, "rb")}
    #file = {'file':open('Etharkkum Thunindhavan - Official Trailer  Suriya  Sun Pictures  Pandiraj  DImman.mp4',"rb")}
    url = 'https://store3.gofile.io/uploadfile'
    description = {'description' :"TRVPN",'tags' : '@trvpn'}
    r = requests.post(url,files= files)

    json_data = r.json()
    print(json_data)

    directory = dest
    try:
        
        await message.reply(f'{json_data}', quote=True)
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
