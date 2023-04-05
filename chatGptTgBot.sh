#!/usr/bin/env bash

read -p "Type your Telegram Bot Token: " tgBotToken
export telegramBotToken=$tgBotToken
read -p "Type your OpenAI API Key: " openAiApi
export openAiApiKey=$openAiApi

python3 main.py

exit 0
