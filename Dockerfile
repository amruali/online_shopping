# Use the official Python image from the Docker Hub
# FROM python:3.6.8-alpine

FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install build dependencies
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    libwebp-dev \
    tiff-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    libpng-dev \
    libxslt-dev \
    libxml2-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Collect static files
# RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8001

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
