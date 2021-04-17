FROM python:3
ENV PYTHONUNBU FFERED 1
# Adds our application code to the image
COPY . code
WORKDIR code

RUN apt-get update -y
RUN apt-get upgrade -y
RUN pip install -r requirements.txt

EXPOSE 8333

# Run the production server
# CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - msof_api.wsgi:application
