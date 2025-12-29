#!/usr/bin/python3
"""
101-stats.py
Reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
Prints metrics every 10 lines and on keyboard interruption (CTRL + C)
"""

import sys


def print_stats(total_size, status_codes):
    """Print the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Try to parse status code and file size from the last two fields
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue  # Ignore lines that cannot be parsed

            # Update totals
            if status in status_codes:
                status_codes[status] += 1
            total_size += size

            # Print every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print stats on CTRL+C
        print_stats(total_size, status_codes)
        raise
    else:
        # Print final stats if EOF reached
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
