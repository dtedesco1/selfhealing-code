import unittest
from unittest.mock import MagicMock, patch
import sys
from io import StringIO
import output


class TestOutput(unittest.TestCase):

    def test_check_and_install_libraries(self):
        with patch('output.subprocess.call') as mock_call:
            requests, bs4 = output.check_and_install_libraries()
            self.assertIsNotNone(requests)
            self.assertIsNotNone(bs4)
            mock_call.assert_not_called()

    def test_extract_top_headlines(self):
        mock_response = MagicMock()
        mock_response.text = '''
        <html>
          <body>
            <h2 class="post-block__title">
              <a href="https://example.com/article1">Article 1</a>
            </h2>
            <h2 class="post-block__title">
              <a href="https://example.com/article2">Article 2</a>
            </h2>
            <h2 class="post-block__title">
              <a href="https://example.com/article3">Article 3</a>
            </h2>
            <h2 class="post-block__title">
              <a href="https://example.com/article4">Article 4</a>
            </h2>
            <h2 class="post-block__title">
              <a href="https://example.com/article5">Article 5</a>
            </h2>
          </body>
        </html>
        '''

        with patch('output.requests.get', return_value=mock_response):
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            output.extract_top_headlines()
            output_str = sys.stdout.getvalue()
            sys.stdout = old_stdout

        expected_output = (
            "1. Article 1\nhttps://example.com/article1\n"
            "2. Article 2\nhttps://example.com/article2\n"
            "3. Article 3\nhttps://example.com/article3\n"
            "4. Article 4\nhttps://example.com/article4\n"
            "5. Article 5\nhttps://example.com/article5\n"
        )

        self.assertEqual(output_str, expected_output)


if __name__ == '__main__':
    unittest.main()