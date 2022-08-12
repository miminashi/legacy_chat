#!/bin/sh

name="$(
  grep '^name=' |
  head -n 1 |
  cut -d '=' -f 2-
)"

printf 'HTTP/1.1 302 Found\r\n'
printf 'Set-Cookie: handleName=%s; Path=/\r\n' "${name}"

printf 'Location: /cgi-bin/index.cgi\r\n'
printf 'Status: 302 Found\r\n'
printf '\r\n'
