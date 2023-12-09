FROM python:3.11.6-slim-bullseye
LABEL maintainer="fido.jiang <jiangzihan@gmail.com>"

ENV TZ "Asia/Shanghai"
ENV PROXY "http://192.168.66.196:8089"

COPY ./requirements.txt /requirements.txt

RUN set -eux; \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free\n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free\n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free\n\
deb https://security.debian.org/debian-security bullseye-security main contrib non-free" > /etc/apt/sources.list; \
    # apt-get update && apt-get install -y ; \
    pip3 install \
    --no-cache-dir --upgrade \
    -r /requirements.txt \
    --proxy=${PROXY}; \
    apt-get autoremove --purge -y; \
    apt-get autoclean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \
    rm -f /requirements.txt;

COPY . /app
WORKDIR /app

ENTRYPOINT ["./startup.sh"]

# docker build -t bgnlp:1.1.8 -f Dockerfile ..