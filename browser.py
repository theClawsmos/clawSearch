# You can only search with the google bar BTW

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("theClawsmos Search")
        self.setCentralWidget(QWidget(self))

        layout = QVBoxLayout(self.centralWidget())
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.returnPressed.connect(self.load_url)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<-")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton("->")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        layout.addLayout(self.horizontal)
        layout.addWidget(self.browser)

        self.go_btn.clicked.connect(self.load_url)
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.browser.setUrl(QUrl("https://google.com"))

        # Apply style sheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 2px;
                font-size: 12px;
            }
            
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 5px 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;
                border-radius: 3px;
            }
            
            QPushButton:hover {
                background-color: #45a049;
            }
        """)


    def load_url(self):
        url = self.url_bar.text()
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = MyWebBrowser()
window.show()
app.exec()






















#If you scroll down this far... Well done. 🎉🎉🎉
