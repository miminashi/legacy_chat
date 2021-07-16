#!/bin/sh
# vi: ft=sh

encodedHandleName=$(echo $HTTP_COOKIE| tr ';' '\n' | tr -d ' ' | grep '^handleName=' | cut -d '=' -f 2)

grep '^text=' |
  head -n 1 |
  cut -d '=' -f 2- |
  sed 's/%/\\x/g' |
  while read -r l; do
    #printf '%b\n' "${l}"
    /usr/bin/printf '%s,%b\n' "${encodedHandleName}" "${l}"
  done >> log

printf 'Location: /cgi-bin/index.cgi\n'
printf 'Status: 302 Found\n\n'
