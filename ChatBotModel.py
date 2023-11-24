import schedule
import time
import telegram
import pytz
import datetime
import asyncio

#Develop a bot that receives text from a created Telegram channel
async def send_telegram_message():

    token = "6597126262:AAFGokjb7XwOXA9k8jLqStQjqa0tUxV2nz0"
    #chat_id: 6863881370
    public_chat_name = '@ai202111616project'
    text = "[AI오픈소스SW실습 alarm] It's half past one."

    bot = telegram.Bot(token = token)
    await bot.send_message(chat_id=public_chat_name, text=text)


count = 1

#Python script for time checking
async def job(): 

    global count
    count += 1
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    time = now.strftime("%H:%M:%S")

    if now.hour >= 23 or now.hour <= 6: #No message output allowed from 11 PM to 6 AM
        return
    else:
        print("[",time,"]","Send a message")
        await send_telegram_message()


# Schedule the job to run every 30 minutes
schedule.every(30).minutes.do(lambda: asyncio.run(job()))
print("Start App")


# Python scheduler. Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1) #Pause the script for 1 second