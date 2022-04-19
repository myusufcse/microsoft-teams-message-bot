FROM python:slim

WORKDIR /usr/src/app

RUN pip install pymsteams sys

COPY runner.py ./

CMD [ "python", "./runner.py" ]