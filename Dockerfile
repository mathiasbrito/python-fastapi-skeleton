FROM python:3.10-alpine

RUN python3 -m pip install --upgrade pip setuptools wheel
RUN apk add --no-cache tini

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install .


EXPOSE 8000

ENTRYPOINT ["/sbin/tini", "--"]
CMD app

