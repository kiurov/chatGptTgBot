import openai
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


telegramBotToken = '5842336746:AAG9ZTvZo-voV0m8QurgEgOwaJ0LSs-z5lI'
openai.api_key = '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'

bot = Bot(telegramBotToken)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)