FROM python:3.9

WORKDIR /IDK


COPY requirements.txt .
COPY ./blog ./blog

RUN pip install -r requirements.txt

CMD [ "python", "/blog/manage.py" ]

