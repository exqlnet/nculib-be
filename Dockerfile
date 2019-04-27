FROM python:3.6
MAINTAINER Exqlnet <exqlnet@gmail.com>

ENV TZ=Asia/Shanghai
ENV FLASK_CONFIG=production

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install freetds-dev build-essential -y && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoclean

COPY requirement.txt /tmp/requirement.txt

RUN pip install -r /tmp/requirement.txt --no-cache-dir --disable-pip-version-check


CMD ["uwsgi", "--ini", "/nculib-be/nculib-uwsgi.ini"]