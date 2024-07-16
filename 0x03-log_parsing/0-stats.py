#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_metrics(file_size, status_codes):
    """
    Print metrics
    """
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    file_size_total = 0
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                
                if len(parts) < 7:
                    continue  # Skip lines that don't have enough parts
                
                # Extract status code and file size
                status_code = parts[-2]
                file_size = parts[-1]

                # Ensure file_size is a valid integer
                try:
                    file_size = int(file_size)
                except ValueError:
                    continue

                # Update file size total
                file_size_total += file_size

                # Update status code count
                if status_code in codes_count:
                    codes_count[status_code] += 1

                count += 1

                if count == 10:
                    print_metrics(file_size_total, codes_count)
                    count = 0
            except Exception:
                continue
    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_count)
        raise
    print_metrics(file_size_total, codes_count)
