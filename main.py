from telethon import TelegramClient
import os

# اطلاعات ربات
api_id = 'YOUR_API_ID'  # از my.telegram.org دریافت کنید
api_hash = 'YOUR_API_HASH'  # از my.telegram.org دریافت کنید
bot_token = 'YOUR_BOT_TOKEN'  # توکنی که از BotFather دریافت کردید
channel_username = 'YOUR_CHANNEL_USERNAME'  # نام کاربری کانال (یا آیدی عددی کانال)

# اتصال به تلگرام
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def remove_duplicate_posts():
    messages = {}  # دیکشنری برای ذخیره هش فایل‌ها
    async for message in client.iter_messages(channel_username):
        if message.file:  # فقط پیام‌هایی که فایل دارند
            file_hash = (message.file.md5_checksum, message.file.size)  # ایجاد هش فایل
            if file_hash in messages:
                await client.delete_messages(channel_username, message.id)  # حذف پیام تکراری
                print(f"Deleted duplicate message: {message.id}")
            else:
                messages[file_hash] = message.id

with client:
    client.loop.run_until_complete(remove_duplicate_posts())
