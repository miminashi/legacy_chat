FROM busybox

COPY ./app/var/www /var/www
COPY ./app/usr/local/bin/* /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

CMD ["start.sh"]
