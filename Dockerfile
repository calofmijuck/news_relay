FROM python:latest

RUN apt update && apt install cron -y && service cron start

RUN mkdir news_relay
ADD news_relay /news_relay/

RUN pip3 install -r /news_relay/requirements.txt

RUN chmod 0744 /news_relay/crontab && cp /news_relay/crontab /etc/cron.d/cron

RUN crontab /etc/cron.d/cron

RUN apt install vim -y

ENTRYPOINT [ "cron", "-f"]
