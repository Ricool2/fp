FROM python:latest
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "main.py" ]