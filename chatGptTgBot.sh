#!/usr/bin/env bash
# Comment
ps -aef | egrep chatGptTgBot.py | grep -v grep
if [ $? -ne 0 ]; then 
    # Run the bot
    /usr/bin/python3 chatGptTgBot.py &

    echo
    echo "Done! Process ID is:"
    ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}'
    bash ~/telegramMessage/telegramMessage.sh -m "ChatGPT - KAK CHLVK was started! $(ps -aef | gawk '$NF~"^chatGptTgBot.py"{print $2,$NF}')"
fi
