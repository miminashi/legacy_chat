FROM busybox

COPY ./app/var/www /var/www
COPY ./app/usr/local/bin/* /usr/local/bin/

CMD httpd -f -vv -h /var/www

#
# docker run の場合: --init オプション
# docker compose の場合: init: true をそれぞれ使う必要がある
#
# 参考: https://text.superbrothers.dev/200328-how-to-avoid-pid-1-problem-in-kubernetes/
#
