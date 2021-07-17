FROM debian:buster-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && \
    apt-get -y install --no-install-recommends lighttpd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN rm -rf /var/www/*
COPY app/var/www/ /var/www/
COPY app/etc/lighttpd/* /etc/lighttpd/
COPY app/usr/local/bin/* /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh
RUN useradd -s /usr/sbin/nologin lighttpd

EXPOSE 80

VOLUME /var/www/cgi-bin/log

CMD ["start.sh"]
