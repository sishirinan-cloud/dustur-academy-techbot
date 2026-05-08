import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiohttp import web

# ТОКЕН
API_TOKEN = '8604668488:AAHsI0d1NIJHR8PoqoXJC5wELEXjInr2w2g'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Код для обхода ограничений Render (создаем пустой веб-сервер)
async def handle(request):
    return web.Response(text="Bot is running")

async def on_startup(dispatcher):
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()

# ВАШИ КОМАНДЫ БОТА
@dp.message(Command("start"))
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📜 Памятка (ВАЖНО)"))
    builder.row(types.KeyboardButton(text="🔑 Как войти в Moodle"))
    builder.row(types.KeyboardButton(text="🆘 Техподдержка"))
    await message.answer("Ассаляму алейкум! Выберите раздел:", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message()
async def actions(message: types.Message):
    if message.text == "📜 Памятка (ВАЖНО)":
        await message.answer("🚫 НЕ НАЖИМАЙТЕ 'СКАЧАТЬ'! Это сломает плеер Bunny.net.")
    elif message.text == "🔑 Как войти в Moodle":
        await message.answer("🌐 Сайт: https://study.dusturacademy.com")
    elif message.text == "🆘 Техподдержка":
        await message.answer("Пишите админу: @ВАШ_НИК")

async def main():
    await on_startup(dp) # Запуск фейкового сервера
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
