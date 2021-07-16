#!/bin/sh

name=$(
  grep '^name=' |
  head -n 1 |
  cut -d '=' -f 2-
)

printf 'Set-Cookie: handleName=%s; Path=/\n' $name

printf 'Location: /cgi-bin/index.cgi\n'
printf 'Status: 302 Found\n\n'
