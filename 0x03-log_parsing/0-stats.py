#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one,
the line must be skipped)
"""
import re


def main():
    """
    Main parses the logs(from input) and prints out the stats based
    passed for every 10 logs that was parsed.
    """
    general_re = re.compile(r'"(?:.*)"|(?:\[.*\])|(?:\S+)')
    valid_codes = [
        200, 301, 400, 401, 403, 404, 405, 500
    ]
    count = 0
    map_code_count = {}
    total_file_size = 0
    try:
        while True:
            read_stdin = input()
            matches = re.findall(general_re, read_stdin)
            if len(matches) != 6:
                continue
            if matches[1] != '-':
                continue
            if not all([matches[2].startswith('['), matches[2].endswith(']')]):
                continue
            if not all([matches[3].startswith('"'), matches[3].endswith('"')]):
                continue
            if matches[3].strip('"') != "GET /projects/260 HTTP/1.1":
                continue
            try:
                get_code = int(matches[4])
                get_file_size = int(matches[5])
            except:
                continue
            if get_code not in set(valid_codes):
                continue
            count += 1
            total_file_size += get_file_size
            map_code_count[get_code] = map_code_count.get(get_code, 0) + 1
            if count == 10:
                print("File size: {}".format(total_file_size))
                for code in valid_codes:
                    if map_code_count.get(code) is None:
                        continue
                    print("{}: {}".format(code, map_code_count[code]))
                count = 0
    except KeyboardInterrupt:
        print("File size: {}".format(total_file_size))
        for code in valid_codes:
            if map_code_count.get(code) is None:
                continue
            print("{}: {}".format(code, map_code_count[code]))
    except Exception as e:
        print("File size: {}".format(total_file_size))
        for code in valid_codes:
            if map_code_count.get(code) is None:
                continue
            print("{}: {}".format(code, map_code_count[code]))


if __name__ == "__main__":
    main()
