#!/usr/bin/python3
"""
    Takes a URL and sends a request to the URL and displays
    the value of "X-request-Id" found in the header response
"""

if __name__ == "__name__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
