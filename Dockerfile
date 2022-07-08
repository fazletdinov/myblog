FROM python:3.9.6-alpine
WORKDIR /usr/src/mysite
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/mysite/entrypoint.sh
RUN chmod +x /usr/src/mysite/entrypoint.sh
COPY . .
ENTRYPOINT ["/usr/src/mysite/entrypoint.sh"]