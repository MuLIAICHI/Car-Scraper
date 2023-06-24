from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import shutil
from scraper import Scraping


class ScraperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScraperJson")
        self.setWindowIcon(QIcon("./images/ai.jpg"))

        self.keyword_entry = QLineEdit()
        self.filename_entry = QLineEdit()

        self.start_button = QPushButton("Start Scraping")
        self.start_button.clicked.connect(self.start_scraping)

        self.download_button = QPushButton("Download JSON")
        self.download_button.clicked.connect(self.download_json)
        self.download_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Create a QLabel for the title
        title_label = QLabel("ScraperJson")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px; text-align: center")

        # Create QLabel widgets for the input fields
        keyword_label = QLabel("Keyword: ")
        keyword_label.setStyleSheet("font-weight: bold; margin-bottom: 5px;")

        filename_label = QLabel("Name Your File: ")
        filename_label.setStyleSheet("font-weight: bold; margin-bottom: 5px;")

        # Set styles for the buttons
        self.start_button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 10px 20px; }"
            "QPushButton:hover { background-color: #45a049; }"
            "QPushButton:pressed { background-color: #3c903c; }"
        )

        self.download_button.setStyleSheet(
            "QPushButton { background-color: #008CBA; color: white; font-weight: bold; padding: 10px 20px; }"
            "QPushButton:hover { background-color: #006F8C; }"
            "QPushButton:pressed { background-color: #00576B; }"
        )

        # Add the widgets to the layout
        layout.addWidget(title_label)
        layout.addWidget(keyword_label)
        layout.addWidget(self.keyword_entry)
        layout.addWidget(filename_label)
        layout.addWidget(self.filename_entry)
        layout.addWidget(self.start_button)
        layout.addWidget(self.download_button)

        # Set the layout for the main window
        self.setLayout(layout)
        self.scraper = Scraping(self)

    def start_scraping(self):
        keyword = self.keyword_entry.text()
        filename = self.filename_entry.text()
        self.scraper.scrape_data(keyword, filename)
        self.download_button.setEnabled(True)
    
    def show_completion(self):
        # Show a message box with the completion message
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("Scraping Completed")
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setText("The scraping process is finished.")
        self.msg_box.setInformativeText("You can proceed with downloading the file.")
        self.msg_box.exec_()

    def download_json(self):
        filename = self.filename_entry.text()

        save_location, _ = QFileDialog.getSaveFileName(self, "Save JSON File", filename, "JSON Files (*.json)")

        if save_location:
            try:
                file_path = f"{filename}.json"
                shutil.copy(file_path, save_location)

                msg_box = QMessageBox()
                msg_box.setWindowTitle("Download Completed")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("The JSON file has been successfully downloaded.")
                msg_box.exec_()
            except Exception as e:
                print("An error occurred while downloading the file:")
                print(str(e))
