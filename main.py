"""
description: Script utility to create request header on the fly upon user provided length.
             Request headers will ultimately send to an user defined endpoint and it will capture the response.
author: Jaziel Lopez <jazlopez @ github.com>
"""

import time
import requests
import argparse
import secrets
from string import ascii_lowercase, digits

parser = argparse.ArgumentParser(description="Create request headers upon kb length size", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-u", "--url", required=True, type=str, help="URL to send request along headers")
parser.add_argument("-s", "--size", required=True, type=int, help="Header size in kilobytes")
parser.add_argument("-t", "--total", required=True, type=int, help="Numbers of headers to be created")
args = parser.parse_args()


def build_header_body(bytes=None, alphabet=ascii_lowercase + digits):
    """
    :param bytes:
    :param alphabet:
    :return:
    """
    return ''.join(secrets.choice(alphabet) for _ in range(bytes))

# -----  PROGRAM BEGINS HERE --------


if not args.total > 0:
    raise RuntimeError("Total headers argument should be greater than 0")

request_headers = {}
url = args.url
number_of_headers = args.total
bytes = args.size * 1024
results = list(map(lambda _: build_header_body(bytes=bytes), list(range(number_of_headers))))

print("------------------------------------------------------")
print(".... program arguments:")
print(f".... server url: {url}")
print(f".... headers: {number_of_headers}")
print(f"...  kb per header: {args.size}")
print("------------------------------------------------------")
print("... please wait")
time.sleep(1)
for i, result in enumerate(results):
    header_name = f"x-custom-{i}"
    header_kilo_bytes = int(len(result.encode('utf-8')) / 1024)
    print(f"........ creating a new header named {header_name} with content size of {header_kilo_bytes}kb")
    request_headers.update({header_name:result})
    time.sleep(1)

print(f".... sending request to {url}")
response = requests.get(url=url, headers=request_headers)
time.sleep(1)
print(f".... receiving response code:{response.status_code}")
time.sleep(1)
print(f"........ {response.text}")
print("...good bye")

# print(results)


# example =
# bb = len(example.encode('utf-8'))
# print(example)
# print(bb)
