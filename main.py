import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5053187040:AAHMorEJ33__FZblZzd63G3KcGHNSHAB-cY')
dp = Dispatcher(bot)

@dp.message_handler(content_types=["photo"])
async def add_image(message: types.Message):
    await message.photo[-1].download('image/image.png')
    await asyncio.sleep(1)
    await message.reply(f"<b>🚀 Изображение успешно загружено!</b>", parse_mode='html')
    await asyncio.sleep(1)
    await message.reply(f"<b>📸 Введите данную команду для создания водяной метки:</b> <code>/text [font] [size] [text]</code>!\n<b>✏️ Шрифты доступные в боте:</b>\n1️⃣ <code>minecraft</code>\n2️⃣ <code>neon</code>", parse_mode='html')

@dp.message_handler(commands=['text'])
async def photo(message: types.Message):
    im = Image.open('image/image.png')
    width, height = im.size
    draw = ImageDraw.Draw(im)
    ttf = message.text.split()[1]
    size_image = message.text.split()[2]
    text = message.text.split()[3]
    if ttf == "neon":
       font = ImageFont.truetype('font/neon.ttf', int(size_image))
       textwidth, textheight = draw.textsize(text, font)
  
    if ttf == "minecraft":
       font = ImageFont.truetype('font/minecraft.ttf', int(size_image))
       textwidth, textheight = draw.textsize(text, font)
    
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text, font=font)
    im.show()
    im.save('image/watermark.png')

    get_photo = open('image/watermark.png', 'rb')
    await message.bot.send_photo(chat_id=message.chat.id, photo=get_photo, caption=f'🚀 Держи!')
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
