import sys
import os
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

# Adjust the import path to the location of the main.py file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from main import ScraperApp


class TestMain(unittest.TestCase):
    def setUp(self):
        # Create a QApplication instance
        self.app = QApplication(sys.argv)

        # Create an instance of ScraperApp
        self.window = ScraperApp()

    def tearDown(self):
        # Clean up resources
        self.window.close()
        del self.window
        del self.app

    def test_gui_elements(self):
        # Test the initial state of GUI elements
        self.assertEqual(self.window.keyword_entry.text(), "")
        self.assertEqual(self.window.filename_entry.text(), "")
        self.assertFalse(self.window.download_button.isEnabled())

        # Test button click and GUI updates
        self.window.keyword_entry.setText("test")
        self.window.filename_entry.setText("test_data.json")
        QTest.mouseClick(self.window.start_button, Qt.LeftButton)

        # Check if the download button is enabled after scraping
        self.assertTrue(self.window.download_button.isEnabled())

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
