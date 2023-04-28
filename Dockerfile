FROM python:3-slim

WORKDIR /app

# COPY requirements.txt requirements.txt
RUN pip3 install openai telebot loguru

COPY . .

CMD [ "python", "chatGptTgBot.py" ]
