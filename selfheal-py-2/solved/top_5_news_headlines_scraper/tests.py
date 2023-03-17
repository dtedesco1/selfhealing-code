from unittest import TestCase
from unittest.mock import Mock, patch
import output
import requests
import bs4

class TestOutput(TestCase):

    def test_install_libraries(self):
        with patch('output.os.system') as mock_os_system:
            output.install_libraries()
            mock_os_system.assert_any_call('pip install requests beautifulsoup4')

    def test_get_top_headlines(self):
        mock_response = Mock()
        content = '''
        <html>
            <body>
                <div class="gs-c-promo-heading__title">Headline 1</div>
                <div class="gs-c-promo-heading__title">Headline 2</div>
                <div class="gs-c-promo-heading__title">Headline 3</div>
                <div class="gs-c-promo-heading__title">Headline 4</div>
                <div class="gs-c-promo-heading__title">Headline 5</div>
            </body>
        </html>
        '''
        mock_response.content = content.encode()
        with patch('requests.get', return_value=mock_response):
            headlines = output.get_top_headlines('https://www.example.com')
            self.assertEqual(len(headlines), 5)
            self.assertEqual(headlines[0][0], 'Headline 1')
            self.assertEqual(headlines[1][0], 'Headline 2')
            self.assertEqual(headlines[2][0], 'Headline 3')
            self.assertEqual(headlines[3][0], 'Headline 4')
            self.assertEqual(headlines[4][0], 'Headline 5')

    def test_main(self):
        with patch('output.get_top_headlines', return_value=[]):
            with patch('output.print') as mock_print:
                output.main()
                mock_print.assert_not_called()