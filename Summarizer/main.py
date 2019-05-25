import sys
from TextSummarizer import Ui_MainWindow
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from app_helpers import read_file, read_url, count_sentences, get_file_menu_help, get_summarization_help, \
    get_general_help
from link_reader import Ui_LinkReader
from TextRank.textrank import TextRankSummarizer
from urllib.parse import urlparse
import data

class GUIForm(QMainWindow):
    """Class representing app main window"""
    def __init__(self, parent=None):
        """Method initializes instance of GUIFrom class
        
        Args:
            QMainWindow ([type]): [description]
            parent (parent object, optional): Parent object to draw form. Defaults to None.
        """
        super(GUIForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.Summarizer = TextRankSummarizer("english")
        self.ui.setupUi(self)
        self.ui.plainTextEdit.textChanged.connect(self.edit_text)
        self.ui.actionOpen_text_file.triggered.connect(self.open_file_dialog)
        self.ui.actionOpen_text_from_url.triggered.connect(self.open_url)
        self.ui.pushButton.clicked.connect(self.summarize)
        self.ui.plainTextEdit.textChanged.connect(self.edit_text)
        self.ui.spinBox.setMinimum(0)
        self.ui.spinBox.setMaximum(0)
        self.ui.actionFile_menu_help.triggered.connect(
            self.show_file_menu_help)
        self.ui.actionGeneral_help_2.triggered.connect(self.show_general_help)
        self.ui.actionSummarization_help.triggered.connect(
            self.show_summary_help)

    def show_file_menu_help(self):
        """Method handles file menu help
        """
        QMessageBox.question(self, 'File menu help', get_file_menu_help(), QMessageBox.Ok | QMessageBox.NoButton)

    def show_general_help(self):
        """Method handles general help
        """
        QMessageBox.question(self, 'General help', get_general_help(), QMessageBox.Ok | QMessageBox.NoButton)

    def show_summary_help(self):
        """Method handles summary help
        """
        QMessageBox.question(self, 'Summarization help', get_summarization_help(),
                             QMessageBox.Ok | QMessageBox.NoButton)

    def edit_text(self):
        """Method handles text editing
        """
        self.text = self.ui.plainTextEdit.toPlainText()
        sentences_number = count_sentences(self.text)
        self.ui.label.setText(
            f"{count_sentences(self.text)} sentences in source text")
        self.ui.spinBox.setMaximum(sentences_number)

    def open_url(self):
        """Method handles opening url
        """
        self.window = QMainWindow()
        self.ui_linkreader = Ui_LinkReader()
        self.ui_linkreader.setupUi(self.window)
        self.ui_linkreader.pushButton.setDefault(True)
        self.window.setFixedSize(self.window.width(), self.window.height())
        self.ui_linkreader.pushButton.clicked.connect(self.process_url)
        self.window.show()

    def process_url(self):
        """Method processes url
        """
        url = self.ui_linkreader.textEdit.toPlainText().strip()
        parsed_url = urlparse(url)
        if parsed_url.scheme == "" or parsed_url.netloc == "":
            self.ui.plainTextEdit.setPlainText("Error: Invalid url")
        else:
            content = read_url(url)
            self.ui.plainTextEdit.setPlainText(content)
        self.window.close()

    def summarize(self):
        """Method handles summarization
        """
        if "text" in dir(self):
            self.Summarizer.set_text(self.text)
            try:
                summary = self.Summarizer.get_summary(self.ui.spinBox.value())
                self.ui.textBrowser.setText("\n".join(summary))
            except:
                self.ui.textBrowser.setText(
                    "Error: Can`t summarize source text.\nProbably source text has incorrect grammar.\nCorrect source "
                    "text and try again. "
                )

    def open_file_dialog(self):
        """Method handles opening file dialog
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Select text file",
                                                  "",
                                                  "Text Files(*);;",
                                                  options=options)
        if fileName:
            try:
                content = read_file(fileName)
                self.ui.plainTextEdit.setPlainText("".join(content))
            except:
                QMessageBox.question(self, 'Error', "Chosen file is not text",
                                     QMessageBox.Ok | QMessageBox.NoButton)


def main():
    data.download_data()
    app = QApplication([])
    style_file = QFile("dark.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(style_file)
    app.setStyleSheet(stream.readAll())
    summarizer_app = GUIForm()
    summarizer_app.setFixedHeight(summarizer_app.height())
    summarizer_app.setFixedWidth(summarizer_app.width())
    summarizer_app.show()
    
    ret = app.exec_()
    sys.exit(ret)


if __name__ == "__main__":
    main()
