FROM python:3.11.6-alpine3.18 as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    libreoffice \
    libreoffice-writer \
    libreoffice-calc \
    libreoffice-impress

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.11.6-alpine3.18

ARG DEBUG=false
ENV PROJECT_DIR=/app
WORKDIR $PROJECT_DIR

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY app application
WORKDIR $PROJECT_DIR/application

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
