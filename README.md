# chatGptTgBot

This code is used to work with chatgpt via the telegram bot. This code was provided by chatgpt. You should have generated tokens for the telegram bot as well as for openai chatgpt in order to use it.

To use run build the docker image:

`docker build --tag chat_gpt_tg_bot_image .`

Then start the docker container by defining the variables `telegramBotToken` and `openAiApiKey`
```
docker run -d \
-e telegramBotToken="<botToken>" \
-e openAiApiKey="<apiKey>" \
--restart=unless-stopped --name chat_gpt_tg_bot_container chat_gpt_tg_bot_image
```

To view the logs, use the command below the container connection
`docker container exec -it chat_gpt_tg_bot_container /bin/bash`