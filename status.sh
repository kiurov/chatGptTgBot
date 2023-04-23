#!/usr/bin/env bash
ps -aef | egrep chatGptTgBot.py | grep -v grep
if [ $? -ne 0 ]; then 
    bash ~/chatGptTgBot/chatGptTgBot.sh -n
    #processId=$(ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}')
    bash ~/telegramMessage/telegramMessage.sh -m "ChatGPT - KAK CHLVK was restarted! $(ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}')"
fi
