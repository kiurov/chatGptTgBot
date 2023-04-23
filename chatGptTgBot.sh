#!/usr/bin/env bash

ps -aef | egrep chatGptTgBot.py | grep -v grep
if [ $? -ne 0 ]; then 
    # Defining the Telegram Bot Token and OpenAI API Key variables in the environment
    if [ "$1" == "-n"  ]; then
        tgBotToken=$(gawk '$1~/^tg$/{print $2}' ~/tockens)
        openAiApi=$(gawk '$1~/^ai$/{print $2}' ~/tockens)
    else
        read -p "Type your Telegram Bot Token: " tgBotToken
        read -p "Type your OpenAI API Key: " openAiApi
    fi
    export telegramBotToken=$tgBotToken
    export openAiApiKey=$openAiApi

    # Run the bot
    python3 chatGptTgBot.py &

    echo
    echo "Done! Process ID is:"
    ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}'
    bash ~/telegramMessage/telegramMessage.sh -m "ChatGPT - KAK CHLVK was started! $(ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}')"
fi



