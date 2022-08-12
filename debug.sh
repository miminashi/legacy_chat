#!/bin/sh

LOG=log.debug

if ! cd "$(dirname "${0}")"; then
  {
    echo "カレントディレクトリの移動に失敗しました"
    echo "終了します"
  } >&2
  exit 1
fi

if ! [ -f "${LOG}" ]; then
  printf '' > "${LOG}"
  chmod o+w "${LOG}"
fi

docker build -t legacy_chat . &&
  docker run --rm -it -v "$(pwd)"/"${LOG}":/var/www/cgi-bin/log -p 8080:80 legacy_chat
