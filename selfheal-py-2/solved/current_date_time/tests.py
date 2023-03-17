import datetime
import output
from io import StringIO
import sys

def test_print_current_datetime():
    saved_stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        output.print_current_datetime()
        output_datetime = sys.stdout.getvalue().strip()
        parsed_datetime = datetime.datetime.strptime(output_datetime, "%Y-%m-%d %H:%M:%S")
    finally:
        sys.stdout = saved_stdout

if __name__ == "__main__":
    test_print_current_datetime()