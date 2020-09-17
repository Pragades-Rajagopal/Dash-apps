FROM python:3.8.3-alpine

WORKDIR /app

RUN apk --update add --no-cache g++

COPY requirement.txt .
RUN pip install -r requirement.txt

COPY /app .

CMD [ "python", "app.py" ]