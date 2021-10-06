FROM python:3.8.5-slim
RUN pwd
RUN mkdir /app
RUN pwd
COPY ./ravon_taxi/ /app/ravon_taxi/
WORKDIR /app/ravon_taxi
RUN ls
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get -y install libpq-dev gcc gdal-bin libgdal-dev\
    && pip install psycopg2


RUN apt-get -y install supervisor
# Install dependencies
RUN pwd
RUN pip install --upgrade pip && pip install --no-cache-dir -r ./requirements/base.txt
RUN pwd

RUN chmod a+rx /app/ravon_taxi/entrypoint.sh
RUN mkdir /etc/supervisor.d/
RUN cp ./supervisord.conf /etc/supervisor/conf.d/
ENTRYPOINT ["/app/ravon_taxi/entrypoint.sh"]
