FROM python:3-alpine

COPY * /apps/subredditfetcher/
WORKDIR /apps/subredditfetcher/
RUN ["pip", "install", "-r", "requirements.txt"]

ENV NBT_ACCESS_TOKEN="824573243:AAGDAhzVBhVV9H36PhoBnFueIEu2IQQAq1Y"

CMD ["python", "newsbot.py"]
