import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# СЮДА ВСТАВЬТЕ ВАШ ТОКЕН ОТ BOTFATHER
API_TOKEN = '8604668488:AAHsI0d1NIJHR8PoqoXJC5wELEXjInr2w2g'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📜 Памятка (ВАЖНО)"))
    builder.row(types.KeyboardButton(text="🔑 Как войти в Moodle"))
    builder.row(types.KeyboardButton(text="🆘 Техподдержка"))
    
    await message.answer(
        "Ассаляму алейкум! Это официальный бот Dustur Academy.\nВыберите нужный раздел ниже:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message()
async def actions(message: types.Message):
    if message.text == "📜 Памятка (ВАЖНО)":
        text = (
            "🚫 **ГЛАВНОЕ ПРАВИЛО:** Ни в коем случае не нажимайте кнопку 'СКАЧАТЬ' на уроках!\n\n"
            "Это защищенный контент Bunny.net. Попытка скачивания блокирует плеер и может вызвать сбой системы. "
            "Смотрите уроки только онлайн внутри платформы."
        )
        await message.answer(text, parse_mode="Markdown")
        
    elif message.text == "🔑 Как войти в Moodle":
        await message.answer(
            "🌐 Адрес платформы: https://study.dusturacademy.com\n\n"
            "📱 Если используете приложение Moodle:\n"
            "1. Введите адрес сайта.\n2. Введите ваш логин/пароль."
        )
        
    elif message.text == "🆘 Техподдержка":
        await message.answer(
            "Если у вас возникла проблема, напишите в личные сообщения: @ВАШ_НИК_В_ТГ\n"
            "Обязательно пришлите скриншот ошибки!"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
