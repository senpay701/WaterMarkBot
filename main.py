import logging
import asyncio
import os
import keyboard as kb
from aiogram import Bot, Dispatcher, executor, types
from PIL import Image, ImageDraw, ImageFont
from glitch_this import ImageGlitcher

glitcher = ImageGlitcher()

logging.basicConfig(level=logging.INFO)

bot = Bot(token='TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message):
    await message.reply(f"<b>🚀 Чтобы начать работу с ботом пришли изображение на котором нужно создать водяной знак.</b>", parse_mode='html', reply_markup=kb.start_ttf)

@dp.message_handler(content_types=["photo"])
async def add_image(message: types.Message):
    user_id = message.from_user.id
    await message.photo[-1].download(f'image/image_{user_id}.png')
    await message.reply(f"<b>🚀 Изображение успешно загружено!</b>", parse_mode='html')
    await message.reply(f"<b>📸 Введите данную команду для создания водяной метки:</b> <code>/text [шрифт] [размер] [цвет] [текст]</code>!\n<b>✏️ Шрифты доступные в боте:</b>\n\n1️⃣ <code>minecraft</code>\n2️⃣ <code>neon</code>\n3️⃣ <code>evil</code>\n4️⃣ <code>gaffuk</code>\n5️⃣ <code>commic</code>\n6️⃣ <code>gagalin</code>\n7️⃣ <code>lettera</code>\n8️⃣ <code>tribute</code>\n9️⃣ <code>marvin</code>\n🔟 <code>patsy</code>\n\n<b>🎨 Цвета доступные в боте:</b>\n⚫️ <code>black</code>\n⚪️ <code>white</code>\n🔴️ <code>red</code>\n🟠 <code>orange</code>\n🟡️ <code>yellow</code>\n🟢️ <code>green</code>\n🔵️ <code>blue</code>\n🔘 <code>gray</code>", parse_mode='html')

@dp.message_handler(commands=['text'])
async def photo(message: types.Message):
    user_id = message.from_user.id
    im = Image.open(f'image/image_{user_id}.png')
    width, height = im.size
    draw = ImageDraw.Draw(im)
    ttf = message.text.split()[1]
    size_image = message.text.split()[2]
    color = message.text.split()[3]
    text = " ".join(message.text.split()[4:])
    if ttf == "neon":
       font = ImageFont.truetype('font/neon.ttf', int(size_image))
     
    if ttf == "minecraft":
       font = ImageFont.truetype('font/minecraft.ttf', int(size_image))
    
    if ttf == "evil":
       font = ImageFont.truetype('font/evil.ttf', int(size_image))
    
    if ttf == "gaffuk":
       font = ImageFont.truetype('font/gaffuk.ttf', int(size_image))
    
    if ttf == "comic":
       font = ImageFont.truetype('font/comic.ttf', int(size_image))
    
    if ttf == "gagalin":
       font = ImageFont.truetype('font/gagalin.ttf', int(size_image))

    if ttf == "lettera":
       font = ImageFont.truetype('font/lettera.ttf', int(size_image))

    if ttf == "marvin":
       font = ImageFont.truetype('font/marvin.ttf', int(size_image))

    if ttf == "patsy":
       font = ImageFont.truetype('font/patsy_sans.ttf', int(size_image))

    if ttf == "tribute":
       font = ImageFont.truetype('font/tribute.ttf', int(size_image))

    textwidth, textheight = draw.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text, fill=color, font=font)
    im.save(f'image/watermark_{user_id}.png')

    get_photo = open(f'image/watermark_{user_id}.png', 'rb')

    glitch_img = glitcher.glitch_image(f'image/image_{user_id}.png', 2, color_offset=True, gif=True)                  
    glitch_img[0].save(f'image/glitch_{user_id}.gif', format='GIF', append_images=glitch_img[1:], save_all=True, duration=200, loop=0)

    await message.bot.send_photo(chat_id=message.chat.id, photo=get_photo, caption=f'<b>🚀 Держи!</b>', parse_mode='html', reply_markup=kb.glitch)
    await asyncio.sleep(20)
    os.remove(f'image/image_{user_id}.png')
    os.remove(f'image/watermark_{user_id}.png')
    os.remove(f'image/glitch_{user_id}.gif')

@dp.callback_query_handler(lambda c: c.data == "font_ttf")
async def start(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, f'<b>✏ Доступные шрифты:</b>\n1️⃣ <code>minecraft</code>\n2️⃣ <code>neon</code>\n3️⃣ <code>evil</code>\n4️⃣ <code>gaffuk</code>\n5️⃣ <code>comic</code>\n6️⃣ <code>gagalin</code>\n7️⃣ <code>lettera</code>\n8️⃣ <code>tribute</code>\n9️⃣ <code>marvin</code>\n🔟 <code>patsy</code>', parse_mode='html', reply_markup=kb.download_font)

@dp.callback_query_handler(lambda c: c.data == "font_1")
async def font_1(callback_query: types.CallbackQuery):
    get_font_1 = open(f'font/minecraft.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_1, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_2")
async def font_2(callback_query: types.CallbackQuery):
    get_font_2 = open(f'font/neon.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_2, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_3")
async def font_3(callback_query: types.CallbackQuery):
    get_font_3 = open(f'font/evil.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_3, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_4")
async def font_4(callback_query: types.CallbackQuery):
    get_font_4 = open(f'font/gaffuk.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_4, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_5")
async def font_5(callback_query: types.CallbackQuery):
    get_font_5 = open(f'font/comic.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_5, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_6")
async def font_6(callback_query: types.CallbackQuery):
    get_font_6 = open(f'font/gagalin.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_6, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_7")
async def font_7(callback_query: types.CallbackQuery):
    get_font_7 = open(f'font/lettera.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_7, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_8")
async def font_8(callback_query: types.CallbackQuery):
    get_font_8 = open(f'font/tribute.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_8, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_9")
async def font_9(callback_query: types.CallbackQuery):
    get_font_9 = open(f'font/marvin.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_9, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "font_10")
async def font_10(callback_query: types.CallbackQuery):
    get_font_10 = open(f'font/patsy_sans.ttf', 'rb')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=get_font_10, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "glitch_effect")
async def glitch_effect(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    glitch_gif = open(f'image/glitch_{user_id}.gif', 'rb')
    await bot.send_video(chat_id=callback_query.message.chat.id, video=glitch_gif, caption=f'<b>🚀 Держи!</b>', parse_mode='html')
    os.remove(f'image/glitch_{user_id}.gif')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)