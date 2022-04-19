FROM python:slim

WORKDIR /usr/src/app

RUN pip install pymsteams

COPY runner.py ./runner.py

ENTRYPOINT [ "python", "./runner.py" ]