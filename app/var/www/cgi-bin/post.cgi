#!/bin/sh
# vi: ft=sh

encodedHandleName="$(echo "${HTTP_COOKIE}" | get_handle_name)"

grep '^text=' |
  head -n 1 |
  cut -d '=' -f 2- |
  uri_decode |
  while read -r l; do
    printf '%s,%s\n' "${encodedHandleName}" "${l}"
  done >> log

printf 'HTTP/1.1 302 Found\r\n'
printf 'Location: /cgi-bin/index.cgi\n'
printf 'Status: 302 Found\n\n'
