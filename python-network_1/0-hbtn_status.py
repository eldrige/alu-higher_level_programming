#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches https://alu-intranet.hbtn.io/status
- using the urllib package and a Mozilla user agent.
"""
import urllib.request

if __name__ == '__main__':
    # Create a request object with the Mozilla user agent
    request = urllib.request.Request('https://intranet.hbtn.io/status')
    request.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0')

    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
