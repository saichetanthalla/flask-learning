FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt .
run pip3 install --no-cache-dir -r requirements.txt
copy . .
CMD ["python","app.py"]

