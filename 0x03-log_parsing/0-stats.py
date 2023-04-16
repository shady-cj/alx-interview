#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
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
            get_code = int(matches[4])
            get_file_size = int(matches[5])
            if get_code not in set(valid_codes):
                continue
            count += 1
            total_file_size += get_file_size
            map_code_count[get_code] = map_code_count.get(get_code, 0) + 1
            if count == 10:
                print(f"File size: {total_file_size}")
                for code in valid_codes:
                    if map_code_count.get(code) is None:
                        continue
                    print(f"{code}: {map_code_count[code]}")
                count = 0
    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for code in valid_codes:
            if map_code_count.get(code) is None:
                continue
            print(f"{code}: {map_code_count[code]}")
    except Exception as e:
        print(f"File size: {total_file_size}")
        for code in valid_codes:
            if map_code_count.get(code) is None:
                continue
            print(f"{code}: {map_code_count[code]}")


if __name__ == "__main__":
    main()
