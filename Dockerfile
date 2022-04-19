FROM python:slim

WORKDIR /usr/src/app

RUN pip install pymsteams

COPY runner.py /usr/bin/runner.py

ENTRYPOINT [ "python", "/usr/bin/runner.py" ]