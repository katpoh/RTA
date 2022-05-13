FROM python:3.10.4
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app
ENTRYPOINT ["python"]

CMD ["main.py"]

