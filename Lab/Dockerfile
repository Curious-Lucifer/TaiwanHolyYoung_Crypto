FROM alpine

RUN apk add --no-cache python3 py3-pip socat

RUN pip3 install --upgrade pip && pip3 install --upgrade pycryptodome

RUN mkdir -p /chal
WORKDIR /chal

COPY . /chal

RUN chmod +x ./docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]