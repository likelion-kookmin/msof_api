###########################################
# Generate package wheel files
FROM python:3.8-slim-buster as package
ENV PYTHONUNBU FFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel -w /root/wheels -r requirements.txt

###########################################
# Run django api server
FROM python:3.8.9-slim-buster as builder
ENV PYTHONUNBU FFERED 1

RUN apt-get update -y \
    && apt-get -f install \
    && apt-get upgrade -y \
    && apt-get clean \
    && pip install --upgrade pip

# Install packages
WORKDIR /code
COPY --from=package /root/wheels /root/wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/root/wheels -r requirements.txt

# Adds our application code to the image
COPY . .

EXPOSE 8333

# Run the production server
# CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - msof_api.wsgi:application
