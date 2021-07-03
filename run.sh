#!/bin/sh
docker run --rm -t -v $(pwd)/www:/var/www/localhost/htdocs -v $(pwd)/conf/lighttpd.conf:/etc/lighttpd/lighttpd.conf -v $(pwd)/conf/mod_cgi.conf:/etc/lighttpd/mod_cgi.conf -p 8080:80 sebp/lighttpd
