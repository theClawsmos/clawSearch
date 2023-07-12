# You can only search with the google bar BTW

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

urllist = []

class WebTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.returnPressed.connect(self.load_url)

        self.go_btn = QPushButton("Go")
        self.go_btn.setFixedSize(50, 50)

        self.back_btn = QPushButton("<-")
        self.back_btn.setFixedSize(50, 50)

        self.forward_btn = QPushButton("->")
        self.forward_btn.setFixedSize(50, 50)
        
        self.home_btn = QPushButton("🏠")
        self.home_btn.setFixedSize(50, 50)
        """
        self.reload_btn = QPushButton("🔄️")
        self.reload_btn.setFixedSize(50, 50)"""

        self.browser = QWebEngineView()

        layout.addWidget(self.url_bar)
        layout.addWidget(self.go_btn)
        layout.addWidget(self.back_btn)
        layout.addWidget(self.forward_btn)
        layout.addWidget(self.home_btn)
        """layout.addWidget(self.reload_btn)"""
        layout.addWidget(self.browser)

        self.go_btn.clicked.connect(self.load_url)
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.home_btn.clicked.connect(self.load_google)
        """self.reload_btn.clicked.connect(self.browserreload)"""

        self.browser.setUrl(QUrl("https://google.com"))

    def load_url(self):
        url = self.url_bar.text()
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            urllist.append(url)
        self.browser.setUrl(QUrl(url))
        
    def load_google(self):
        url = 'https://google.com'
        self.browser.setUrl(QUrl(url))
    
    """def browserreload(self):
        self.browser.setUrl(QUrl("https://" + urllist[-1]))"""


class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("theClawsmos Search")
        self.setCentralWidget(QWidget(self))

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        layout = QVBoxLayout(self.centralWidget())
        layout.addWidget(self.tab_widget)

        self.add_tab()

        new_tab_btn = QPushButton("New Tab")
        new_tab_btn.clicked.connect(self.add_tab)
        layout.addWidget(new_tab_btn)

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
        
    def add_tab(self):
        web_tab = WebTab()
        index = self.tab_widget.addTab(web_tab, "New Tab")
        self.tab_widget.setCurrentIndex(index)

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)

    def load_url(self):
        current_tab = self.tab_widget.currentWidget()
        current_tab.load_url()


app = QApplication([])
window = MyWebBrowser()
window.show()
app.exec()



















#If you scroll down this far... Well done. 🎉🎉🎉
