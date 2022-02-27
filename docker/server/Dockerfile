FROM python:3.9-buster

RUN apt update 
RUN useradd server -u 1000 -m

WORKDIR /home/server/app
RUN pip install Flask black

RUN chown -R server:server /home/server