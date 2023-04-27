# chatGptTgBot

This code is used to work with chatgpt via the telegram bot. This code was provided by chatgpt. You should have generated tokens for the telegram bot as well as for openai chatgpt in order to use it.

To run the docker container use the command below by defining the variables `telegramBotToken` and `openAiApiKey`:
```
docker run -d --pull=always --restart=unless-stopped \
--env telegramBotToken="<tgBotToken>" \
--env openAiApiKey="<openAiKey>" \
--name chatgpttgbotcontainer kyurov/chatgpttgbot
```


To connect inside container, use the command below the container connection

`docker container exec -it chat_gpt_tg_bot_container bash`


To view the logs, use the command below the container connection

`docker container exec -it chat_gpt_tg_bot_container cat /app/log/bot.log`