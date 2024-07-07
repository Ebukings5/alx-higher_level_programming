#!/bin/bash
# send a delete request to the URL passed as first arguement and display the body of response

curl -s -X DELETE "${1}"
