FROM python:slim

WORKDIR /usr/src/app

RUN pip install pymsteams

COPY runner.py ./

ENTRYPOINT [ "python", "runner.py" ]