#!/usr/bin/env bash

# Defining the Telegram Bot Token variable in the environment
read -p "Type your Telegram Bot Token: " tgBotToken
export telegramBotToken=$tgBotToken

# Defining the OpenAI API Key variable in the environment
read -p "Type your OpenAI API Key: " openAiApi
export openAiApiKey=$openAiApi

# Run the bot
python3 chatGptTgBot.py &

echo
echo "Done! Process ID is:"
ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}'