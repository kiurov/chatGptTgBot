# Import the necessary libraries
import telebot
import openai
import os

# Define the bot token
telegramBotToken = os.environ["telegramBotToken"]

# Create the bot instance
bot = telebot.TeleBot(telegramBotToken)

# Define the OpenAI API key
openai.api_key = os.environ["openAiApiKey"]

# Define the bot's message handler
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to("Hi, I am an AI-powered bot. Ask me a question and i will do my best to answer it!\nПривет, я бот с искусственным интеллектом. Задайте мне вопрос, и я сделаю все возможное, чтобы ответить на него.")

# Define the bot's response handler
@bot.message_handler(func=lambda message: True)
def answer_question(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=50,
        temperature=0.9,
        top_p=1.0
    )
    bot.reply_to(response['choices'][0]['text'])

# Run the bot
bot.polling()
