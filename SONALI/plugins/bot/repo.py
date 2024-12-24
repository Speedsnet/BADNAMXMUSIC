from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ тєαм 𝐊ʀɪsʜɴᴇᴛᴡᴏʀᴋ 𝐌ᴜsɪᴄ 

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏʀ ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ Bᴀᴅɴᴀᴍ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʀᴇᴘᴏ Jᴀʙ ᴍɪʟᴇɢᴀ

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ ᴋᴏ Bᴀᴅɴᴀᴍ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʀᴇᴘᴏ Jᴀʙ ᴍɪʟᴇɢᴀ

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url=f"https://t.me/syn_ixbot?startgroup=true")
        ],
        [
          InlineKeyboardButton("✰ 𝛅ꭎᴘ፝֠֩ᴘσꝛᴛ ✰", url="https://t.me/krishSUPPORT"),
          InlineKeyboardButton("𝐊ʀɪsʜɴᴇᴛᴡᴏʀᴋ ", url="https://t.me/krishnetwork"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/krishnetwork"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/syn_ixbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/chg2p4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
