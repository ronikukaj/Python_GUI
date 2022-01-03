import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.allow = False
        self.setLayout(qtw.QVBoxLayout())
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        self.components()
        self.show()


    def components(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.line = qtw.QLineEdit()
        self.text_area = qtw.QPlainTextEdit()
        self.enable_editing = qtw.QPushButton('Enable Editing')
        self.disable_editing = qtw.QPushButton('Disable Editing')
        self.save_button = qtw.QPushButton('Save Changes')

        container.layout().addWidget(self.line, 0, 0, 1, 4)
        container.layout().addWidget(self.text_area, 1, 0, 4, 4)

        if self.allow == False:
            container.layout().addWidget(self.enable_editing, 5, 0, 1, 2)
        else:
            container.layout().addWidget(self.disable_editing, 5, 0, 1, 2)

        container.layout().addWidget(self.save_button, 5, 2, 1, 2)

        self.layout().addWidget(container)



if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
