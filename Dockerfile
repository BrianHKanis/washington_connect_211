FROM python:3.11

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir connect_211

WORKDIR /connect_211

COPY . .

CMD ["python3", "console.py"]

