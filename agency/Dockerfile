FROM python:3.9.16 as builder

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/www/agency

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY req.pip .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /srv/www/agency/wheels -r req.pip


FROM python:3.9.16

WORKDIR /srv/www/agency

COPY --from=builder  /srv/www/agency/wheels /wheels
COPY . .

RUN pip install --no-cache /wheels/*


