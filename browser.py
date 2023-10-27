import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,QLineEdit, QPushButton, QMessageBox,QLabel,QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import csv

class UrlButton(QPushButton):
    def __init__(self, text, url,text_input,tab, parent=None):
        super().__init__(text, parent)
        self.url = url
        self.text_input = text_input
        self.clicked.connect(self.show_url)
        self.tab = tab

    def show_url(self):
        text = self.text_input.text()
        url2 = self.url.replace("[SYMBOL]",text)
        wv = QWebEngineView()
        wv.setUrl(QUrl(url2))
        index = self.tab.addTab(wv,text)
        self.tab.setCurrentIndex(index)

          

class WebPageOpener(QMainWindow):
    buttons={}
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thai Stock Browser")
        self.setGeometry(30, 30, 1200, 600)

        # Create the main widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.menu_layout = QHBoxLayout()
        self.layout.addLayout(self.menu_layout)

        # Create a text input field
        self.text_lable = QLabel("SYMBOL:")
        self.text_input = QLineEdit("PTT")
        self.menu_layout.addWidget(self.text_lable)
        self.menu_layout.addWidget(self.text_input)


        self.tab = QTabWidget(self)
        self.tab.tabCloseRequested.connect(self.tab.removeTab)
        self.layout.addWidget(self.tab)


        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("http://www.settrade.com"))         
        self.tab.addTab(self.web_view,"SETTRADE")
        self.tab.setTabsClosable(True)


        
        # Create a button from config file
        self.create_menu()

    def create_menu(self):
        config_file = "url.cfg"
        with open(config_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                text, url = row
                button = UrlButton(text,url,self.text_input,self.tab)
                #button = UrlButton2(text,url)
                self.menu_layout.addWidget(button)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebPageOpener()
    window.show()
    sys.exit(app.exec_())
