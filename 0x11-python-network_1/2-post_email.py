#!/usr/bin/python3
"""
    A script that takes a URL and email and sends a POST request passed to
    the URL with the email as parameter and display the body response(decoded utf-8)
"""

if __name__ == "__name__":
    import sys
    import urllib.request
    import urllib.parse

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    DATA = urllib.request.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
