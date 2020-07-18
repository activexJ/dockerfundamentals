FROM python:3.7.8-alpine3.12

WORKDIR /app
COPY . .

RUN pip install -r requirement.txt

CMD [ "python", "app.py" ]