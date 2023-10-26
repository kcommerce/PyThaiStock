import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton,QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebPageOpener(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thai Stock")
        self.setGeometry(100, 100, 1200, 600)

        # Create the main widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Create the bar  layout
        layout = QHBoxLayout()




        # Create a text input field
        self.text_input = QLineEdit("PTT")
        main_layout.addWidget(self.text_input)

        main_layout.addLayout(layout)
        # Create a web display area
        self.web_view = QWebEngineView()
        main_layout.addWidget(self.web_view)

        # Create a button
        open_button = QPushButton("SiamChart")
        open_button.clicked.connect(self.open_webpage)
        layout.addWidget(open_button)

        open_button2 = QPushButton("Finance")
        open_button2.clicked.connect(self.open_webpage_finance)
        layout.addWidget(open_button2)

        open_button3 = QPushButton("News")
        open_button3.clicked.connect(self.open_webpage_news)
        layout.addWidget(open_button3)

        open_button4 = QPushButton("Info")
        open_button4.clicked.connect(self.open_webpage_info)
        layout.addWidget(open_button4)

        self.open_webpage()


    def open_webpage(self):
        text = self.text_input.text()
        url = "http://siamchart.com/stock-chart/" + text
        self.web_view.setUrl(QUrl(url))
    def open_webpage_finance(self):
        text = self.text_input.text()
        url = "https://www.set.or.th/th/market/product/stock/quote/"+text+"/financial-statement/company-highlights" 
        self.web_view.setUrl(QUrl(url))
    def open_webpage_news(self):
        text = self.text_input.text()
        url = "https://www.set.or.th/th/market/product/stock/quote/"+text+"/news" 
        self.web_view.setUrl(QUrl(url))

    def open_webpage_info(self):
        text = self.text_input.text()
        url = "https://www.set.or.th/th/market/product/stock/quote/"+text+"/company-profile/information"
        self.web_view.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebPageOpener()
    window.show()
    sys.exit(app.exec_())
