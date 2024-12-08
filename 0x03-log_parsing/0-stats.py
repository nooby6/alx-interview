#!/usr/bin/python3
"""Contains a class for handling a log stream"""

import re
import signal
import sys


class CounterDict(dict):
    """Implements a counting dict by setting missing keys to a value of 0"""

    def __missing__(self, key):
        return 0


class LogSession:
    """Defines a log session, keeping tally of log records"""

    def __init__(self):
        self.file_size = 0
        self.status_codes = CounterDict()

    @property
    def status_codes(self) -> CounterDict:
        """status_codes getter"""
        return self._status_codes

    @status_codes.setter
    def status_codes(self, codes: CounterDict):
        """status_codes setter"""
        self._status_codes = codes

    @property
    def file_size(self) -> int:
        """file_size getter"""
        return self._file_size

    @file_size.setter
    def file_size(self, size: int):
        """file_size setter"""
        self._file_size = size

    def parse_line(self, line: str):
        """Parses a log line to extract and update the HTTP status code and
        size"""
        ptn = re.compile(
            r"(?P<ip>(\d{1,3}.){3}\d{1,3}) ?- ?\[(?P<time>([\d:\.\- ])*)\] "
            r'"GET /projects/260 HTTP/1.1" (?P<code>\d{3}) (?P<size>\d{1,4})$'
        )
        match = ptn.match(line)

        if match:
            self.file_size += int(match.group("size"))
            self.status_codes[int(match.group("code"))] += 1

    def print_stats(self):
        """Prints the total file size for the processed logs and occurrences
        of each HTTP code
        """
        print("File size: {}".format(self.file_size))
        for code in sorted(self.status_codes):
            count = self.status_codes.get(code)
            print("{}: {}".format(code, count))

    def signal_handler(self, signum, frame):
        """Handles an intercepted a Ctrl+C signal"""
        self.print_stats()


if __name__ == "__main__":
    logs = LogSession()
    signal.signal(signal.SIGINT, logs.signal_handler)
    lines = 0

    for log in sys.stdin:
        logs.parse_line(log)
        lines += 1

        if not lines % 10:
            logs.print_stats()

    logs.print_stats()
