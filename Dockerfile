FROM python:3.8.5-slim
RUN mkdir /app
COPY ravon_taxi/ /app/ravon_taxi/
WORKDIR /app/ravon_taxi
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2



# Install dependencies
RUN pwd
RUN pip install --upgrade pip && pip install --no-cache-dir -r ./requirements/base.txt
RUN pwd

RUN chmod +x /app/ravon_taxi/entrypoint.sh
EXPOSE 8010
CMD ["/app/ravon_taxi/entrypoint.sh"]