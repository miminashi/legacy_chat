#!/bin/sh
# vi: ft=sh

encodedHandleName="$(echo "${HTTP_COOKIE}" | get_handle_name)"

grep '^text=' |
  head -n 1 |
  cut -d '=' -f 2- |
  uri_decode |
  while read -r l; do
    #printf '%b\n' "${l}"
    /usr/bin/printf '%s,%s\n' "${encodedHandleName}" "${l}"
  done >> log

printf 'Location: /cgi-bin/index.cgi\n'
printf 'Status: 302 Found\n\n'
