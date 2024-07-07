#!/bin/bash
# Display all HTTP methods the server will accept

curl -s -I "${1}" | grep "^allow: .*" | cut -d " " -f 2-
