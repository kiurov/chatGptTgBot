#!/usr/bin/env bash
ps -aef | egrep chatGptTgBot.py | grep -v grep
if [ $? -ne 0 ]
then 
    bash ~/telegramMessage/telegramMessage.sh -m "ChatGPT TG Bot does not work!"
fi
