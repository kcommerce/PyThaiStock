import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QFileDialog,QMainWindow, QTextEdit,QWidget, QVBoxLayout, QHBoxLayout,QLineEdit, QPushButton, QMessageBox,QLabel,QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import csv,os,tempfile


class ConfigEditor(QMainWindow):
    def __init__(self,config_file):
        super().__init__()

        self.init_ui(config_file)

    def init_ui(self,config_file):
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.load_button = QPushButton("Open Config File")
        self.load_button.clicked.connect(self.open_config_file)
        self.layout.addWidget(self.load_button)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_config_file)
        self.layout.addWidget(self.save_button)
        self.save_button.setEnabled(False)

        self.setCentralWidget(self.central_widget)
        self.read_config(config_file)

    def open_config_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(self, "Open Config File", "", "Config Files (*.cfg);;All Files (*)", options=options)

        self.read_config(file_path)

    def read_config(self,file_path):
        if file_path:
            with open(file_path, "r") as file:
                config_content = file.read()
                self.text_edit.setPlainText(config_content)
                self.current_file = file_path
                self.save_button.setEnabled(True)
        else:
            self.show_message_box("Error: Cannot read file:"+file_path)

    def save_config_file(self):
        if hasattr(self, 'current_file'):
            config_content = self.text_edit.toPlainText()
            with open(self.current_file, "w") as file:
                file.write(config_content)
                self.save_button.setEnabled(True)
                self.show_message_box("File saved successfully:"+self.current_file)
    def show_message_box(self,message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Message")
        msg_box.setText(message)
        msg_box.exec_()


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


        # Create Config button
        self.cbutton = QPushButton("Config")
        self.cbutton.clicked.connect(self.show_config)
        self.menu_layout.addWidget(self.cbutton)
        # Create a button from config file
        self.config_file="url.cfg"

        self.default_config="""Menu-Name,URL-with-[SYMBOL]
SiamChart,http://siamchart.com/stock-chart/[SYMBOL]
Finance,https://www.set.or.th/th/market/product/stock/quote/[SYMBOL]/financial-statement/company-highlights
News,https://www.set.or.th/th/market/product/stock/quote/[SYMBOL]/news
Profile,https://www.set.or.th/th/market/product/stock/quote/[SYMBOL]/company-profile/information
"""
        self.create_menu()



    
    def read_default(self):
        config_file = self.config_file
        try:
            f = open(config_file, "w")
            f.write(self.default_config)
            f.close()
            self.read_csv(config_file)    
        except:
            config_file = os.path.join(tempfile.gettempdir(),self.config_file)
            self.show_message_box("Cannot create and read url.cfg from Home directory")  
            self.show_message_box("Try to create file from:"+config_file)
            try:
                f = open(config_file, "w")
                f.write(self.default_config)
                f.close()
                self.read_csv(config_file)  
                # update config file new location
                self.config_file = config_file
            except:
                self.show_message_box("Cannot create and read from "+config_file)  
    def read_csv(self,config_file):
        with open(config_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                text, url = row
                button = UrlButton(text,url,self.text_input,self.tab)
                #button = UrlButton2(text,url)
                self.menu_layout.addWidget(button)   

    def create_menu(self):

        try:

            config_file = self.config_file
            self.read_csv(config_file)

        except:
            self.show_message_box("Error: Missing url.cfg: Open default config")
            self.read_default()

    def show_config(self):
        #self.show_message_box("Hello, World")
        window = ConfigEditor(self.config_file)
        index = self.tab.addTab(window, "Config Editor")
        self.tab.setCurrentIndex(index)

    def show_message_box(self,message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Message")
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebPageOpener()
    window.show()
    sys.exit(app.exec_())
