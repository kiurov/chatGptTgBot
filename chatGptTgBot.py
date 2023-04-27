# Import the necessary libraries
import os
import telebot
import openai
from loguru import logger

logger.add('log/bot.log', format='{time:DD-MM-YY HH:mm:ss} - {level} - {message}', level='INFO', rotation='1 week', compression='zip')


# Define the bot token and create the bot instance
bot = telebot.TeleBot(os.environ["telegramBotToken"])

# Define the OpenAI API key
openai.api_key = os.environ["openAiApiKey"]


# Define the bot's start message handler
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, I am an AI-powered 🧠 bot. Ask me a question and I will do my best to answer it!\n\nПривет, я бот с искусственным 🧠 интеллектом. Задайте мне вопрос и я сделаю все возможное, чтобы ответить на него!")
    # log file
    logger.info(f"{message.from_user.username} Write: {message.text}")

# Define the bot's response handler
@bot.message_handler(func=lambda message: True)
def answer_question(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=4000,
        temperature=0.9,
        top_p=1.0
    )
    bot.send_message(message.chat.id, response['choices'][0]['text'])
    # log file
    logger.info(f"{message.from_user.username} Write: {message.text}")
    
# Run the bot
bot.polling()
