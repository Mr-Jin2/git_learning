FROM python:3.8

WORKDIR ./docker_demo

add . .

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
