FROM python:3.9

COPY ./app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY . /src

EXPOSE 5000

WORKDIR src

CMD ["python3", "app/app.py"]