#!/usr/bin/python3
import sys

# Initialize metrics
total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """Prints the accumulated metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    line_count = 0
    for line in sys.stdin:
        parts = line.split()
        # Verify the format
        if len(parts) < 7:
            continue
        # Extract file size and status code
        file_size = parts[-1]
        status_code = parts[-2]
        # Update total file size
        try:
            total_file_size += int(file_size)
        except ValueError:
            continue
        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1
        # Increment line count
        line_count += 1
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle CTRL + C signal
    print_stats()
    sys.exit(0)

# Print final stats after EOF
print_stats()
