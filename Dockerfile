FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "/app/cli.py" , "/data/input/template.json", "/data/input/customers.csv", "/data/output", "/data/errors/errors.csv"]
