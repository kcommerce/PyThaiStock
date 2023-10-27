import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget, QFileDialog

class ConfigEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
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
        self.read_config("url.cfg")

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
                self.show_message_box("File saved successfully.")
    def show_message_box(self,message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Message")
        msg_box.setText(message)
        msg_box.exec_()

def main():
    app = QApplication(sys.argv)
    window = ConfigEditor()
    window.setWindowTitle("Config Editor")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
