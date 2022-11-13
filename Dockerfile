FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV ENV_TYPE production

COPY . /code

EXPOSE 3205:3205


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3205"]


