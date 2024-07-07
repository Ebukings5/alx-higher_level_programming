#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__name__":
    r = request.get('https://alx-intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
