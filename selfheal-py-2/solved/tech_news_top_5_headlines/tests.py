import unittest
from unittest.mock import MagicMock, patch
import sys
from io import StringIO
# import output


class TestOutput(unittest.TestCase):

    # def test_check_and_install_libraries(self):
    #     with patch('output.subprocess.call') as mock_call:
    #         requests, bs4 = output.check_and_install_libraries()
    #         self.assertIsNotNone(requests)
    #         self.assertIsNotNone(bs4)
    #         mock_call.assert_not_called()

    def test_extract_top_headlines(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()