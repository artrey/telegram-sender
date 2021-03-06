# Base image
FROM python:3-alpine
LABEL maintainer="Alexander Ivanov <oz.sasha.ivanov@gmail.com>"

# Required packages
RUN apk --update --upgrade --no-cache add \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# System envoriments
ENV LANG=C.UTF-8 \
	PYTHONUNBUFFERED=1

WORKDIR /app

# Target requirements
COPY requirements.txt .

# Project's requirements
RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

# Target project
COPY . .

# Valid stopping
STOPSIGNAL SIGINT

# Add main executable script and run it
CMD ["gunicorn", "config.wsgi", "-w", "4", "-t", "600", "-b", "0.0.0.0:8000"]
