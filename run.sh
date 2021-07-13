#!/bin/sh

LOG=log

cd $(dirname $0)

if ! [ -f "${LOG}" ]; then
  printf '' > "${LOG}"
  chmod o+w "${LOG}"
fi

docker run --rm -t -v $(pwd)/"${LOG}":/var/www/cgi-bin/log -p 8080:80 miminashi/legacy_chat
