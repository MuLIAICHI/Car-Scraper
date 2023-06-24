import sys
from PyQt5.QtWidgets import QApplication
from gui import ScraperApp 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScraperApp()

    window.setStyleSheet("background-color: #F5F5F5;")
    window.setFixedSize(400, 300)  # Adjust the size as per your preference

    window.show()
    sys.exit(app.exec_())
