from aiogram import types

start_ttf = types.InlineKeyboardMarkup(row_width=3)
start_ttf.add(types.InlineKeyboardButton(text='✏️ Шрифты', callback_data='font_ttf'))

download_font = types.InlineKeyboardMarkup(row_width=5)
download_font.add(types.InlineKeyboardButton(text='1️⃣ ', callback_data='font_1'), types.InlineKeyboardButton(text='2️⃣ ', callback_data='font_2'), types.InlineKeyboardButton(text='3️⃣', callback_data='font_3'), types.InlineKeyboardButton(text='4️⃣', callback_data='font_4'), types.InlineKeyboardButton(text='5️⃣', callback_data='font_5'))
download_font.add(types.InlineKeyboardButton(text='6️⃣', callback_data='font_6'), types.InlineKeyboardButton(text='7️⃣', callback_data='font_7'), types.InlineKeyboardButton(text='8️⃣', callback_data='font_8'), types.InlineKeyboardButton(text='9️⃣', callback_data='font_9'), types.InlineKeyboardButton(text='🔟', callback_data='font_10'))