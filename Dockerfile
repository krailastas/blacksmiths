FROM python:3.6.4-alpine3.7

RUN apk update && apk add \
        postgresql-dev \
        libc-dev \
        python3-dev \
        gcc \
        nano \
        jpeg-dev \
        openntpd \
        zlib-dev \
        musl-dev \
        linux-headers && \
        mkdir app

WORKDIR /app/

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

ADD . /app/

RUN if [ -s requirements.txt ]; then pip install -r requirements.txt; fi
EXPOSE 8094
VOLUME /app/blacksmiths/assets
VOLUME /app/blacksmiths/media
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8094", "blacksmiths.wsgi:application"]
