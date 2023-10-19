#!/usr/bin/python3
""" The script to count the number of occurrences of status codes """
import sys
import re


def print_statistics(file, status_code_counts):
    print(f"File size: {len(file)}")
    for key in sorted(status_code_counts.keys()):
        print(f"{key}: {status_code_counts[key]}")


ip = r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - '
timestamp = r'\[[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+:[0-9]+\.[0-9]+\] '
http_request = r'"GET /projects/260 HTTP/1\.1" [0-9]+ [0-9]+'

file = ''
index = 1
allowed_codes = [200, 301, 400, 401, 403, 404, 405, 500]
number_of_codes = {}

try:
    for line in sys.stdin:
        file += line
        lst = line.split(' ')
        status_code = int(lst[-2])
        found = re.search(ip + timestamp + http_request, line)
        if status_code not in allowed_codes or found is None:
            index += 1
            continue
        if status_code in number_of_codes:
            number_of_codes[status_code] += 1
        else:
            number_of_codes[status_code] = 1
        if index % 10 == 0:
            print_statistics(file, number_of_codes)
        index += 1

except KeyboardInterrupt:
    print_statistics(file, number_of_codes)
