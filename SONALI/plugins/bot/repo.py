from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ тєαм 𝐊ᴜsʜɪ 𝐌ᴜsɪᴄ 

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏʀ ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ 3 ɢᴄ ᴍᴀɪ ᴀᴅᴅ ᴋᴀʀ ᴋᴇ 

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ ᴋᴏ ᴅᴏ ғɪʀ ʀᴇᴘᴏ ᴍɪʟ sᴀᴋᴛɪ ʜᴀɪ 

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url=f"https://t.me/Kushi_music_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("✰ 𝛅ꭎᴘ፝֠֩ᴘσꝛᴛ ✰", url="https://t.me/TEAM_KRITI_SUPPORT"),
          InlineKeyboardButton("𝐊ᴜsʜɪ _ 𝐌ᴜsɪᴄ ", url="https://t.me/TEAM_KRITI_SUPPORT"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/TEAM_KRITI_SUPPORT"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/Kushi_music_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/arnzab.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
