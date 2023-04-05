import openai
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#telegramBotToken = '<telegramBotToken>'
telegramBotToken = os.environ["telegramBotToken"]
#openai.api_key = '<openAiToken>'
openai.api_key = os.environ["openAiApiKey"]

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