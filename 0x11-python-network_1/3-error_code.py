#!/usr/bin/python3
"""
    A script that takes in a URL and sends a request to the URL and displays
    the body of response (decoded in utf-8
"""

if __name__ == "__name__":
    import sys
    from urllib import request, error

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
        except error.HTTPError as err:
            print("Error code : {}".format(err.status))
