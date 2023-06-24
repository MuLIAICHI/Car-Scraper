import unittest
import os
from unittest.mock import MagicMock, patch
import sys

# Adjust the import path to include the "app" folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from scraper import Scraping


class MockGUI:
    def show_completion(self):
        pass


class TestScraper(unittest.TestCase):
    def setUp(self):
        self.gui = MockGUI()

    @patch('requests.get')  # Patch requests.get for mocking
    def test_scrape_data(self, mock_get):
        # Create an instance of Scraping
        scraper = Scraping(self.gui)

        # Call the scrape_data method with test data
        keyword = 'test'
        filename = 'test_data'

        # Mock the requests.get method
        mock_response = MagicMock()
        mock_response.content = '<html><body>Mock HTML</body></html>'
        mock_get.return_value = mock_response

        scraper.scrape_data(keyword, filename)

        # Assert that the file is created
        self.assertTrue(os.path.exists(f'{filename}.json'))

        # Additional assertions or checks can be performed here

        # Clean up the test data (optional)
        os.remove(f'{filename}.json')


if __name__ == '__main__':
    unittest.main()
