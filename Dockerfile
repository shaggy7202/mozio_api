FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mozio_api.settings
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/

# Install gdal
RUN apt-get update && apt-get install -y libgdal-dev

# Install project dependencies and migrations
RUN pip install -r requirements.txt

EXPOSE 8000
