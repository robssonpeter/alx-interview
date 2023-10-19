#!/usr/bin/python3
""" The script to count the number of occurances of status codes """
import sys
import re


std_in = sys.stdin
pattern = ''

part1 = r'^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]* - '
part2 = r'\[[0-9]*-[0-9]*-[0-9]* [0-9]*\:[0-9]*\:[0-9]*\.[0-9]*\] '
part3 = r'\"GET \/projects\/260 HTTP\/1\\.1\" [0-9]* [0-9]'
file = ''
index = 1
allowed_codes = [200, 301, 400, 401, 403, 404, 405, 500]
number_of_codes = {

}

joined_pattern = part1+part2+part3
try:
    for line in std_in:
        file = file+line
        lst = line.split(' ')
        status_code = int(lst[-2])
        found = re.search(joined_pattern, line)
        if status_code not in allowed_codes or found is None:
            index += 1
            continue
        keys = number_of_codes.keys()

        if status_code in keys:
            number_of_codes[status_code] += 1
        else:
            number_of_codes[status_code] = 1

        if index % 10 == 0:
            print(f"File size: {len(file)}")
            for key in sorted(number_of_codes.keys()):
                print(f"{key}: {number_of_codes[key]}")
        index += 1
except KeyboardInterrupt:
    print
    print(f"File size: {len(file)}")
    for key in sorted(number_of_codes.keys()):
        print(f"{key}: {number_of_codes[key]}")
