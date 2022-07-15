# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip && pip install tzdata
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
#ENTRYPOINT ["/app/entrypoint.sh"]