#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response
curl -sI "$URL" | awk '/Content-Length/ {print $2}' | tr -d '\r'