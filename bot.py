# © mrlokaman , @lntechnical
import os
from pyrogram import Client, filters
import time 
ADMIN = os.environ.get("ADMIN", "")
TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID",12345))
API_HASH = os.environ.get("API_HASH", "")

app = Client("livebot" ,bot_token = TOKEN ,api_hash= API_HASH ,api_id = API_ID)
        
CH_USER_NAME = os.environ.get("CH_USER_NAME", "")
x = []
    
@app.on_message(filters.user(ADMIN) & filters.command("livecount",prefixes='!'))
async def livecount(client,message):
  count1 = await app.get_chat_members_count(CH_USER_NAME)
  ms = await message.reply_text(f"Live Telegram Subscriber Counting\n {CH_USER_NAME} - {count1}")
  while True :
   time.sleep(3)
   count = await app.get_chat_members_count(CH_USER_NAME)   
   try:
      if x[0] == count:
       time.sleep(3)
      else:
       del x[0]
       x.append(count)
       await ms.edit(f"Live Telegram Subscriber Counting\n {CH_USER_NAME} - {x[0]}")
   except :
    x.append(count)
 
app.run()
