#!/bin/sh

LOG=log.debug

cd $(dirname $0)

if ! [ -f "${LOG}" ]; then
  printf '' > "${LOG}"
  chmod o+w "${LOG}"
fi

docker build -t legacy_chat . &&
  docker run --rm -t -v $(pwd)/"${LOG}":/var/www/cgi-bin/log -p 8080:80 legacy_chat
