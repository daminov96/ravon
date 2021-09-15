FROM python:3.8.5-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
# Set some env varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY /requirements /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/base.txt
# Add entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh


RUN chmod +x /app/entrypoint.sh
# Copy project
COPY src /app
# Run server
CMD ["/app/entrypoint.sh"]