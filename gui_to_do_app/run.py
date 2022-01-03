import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sqlite3

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('To Do Application')
        self.setLayout(qtw.QVBoxLayout())
        self.setStyleSheet("background-color: #DCDCDC;")
        self.components()
        self.show()

    def components(self):

        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        to_do_label = qtw.QLabel('To do')
        self.to_do_list = qtw.QListWidget()
        finished_label = qtw.QLabel('Finished')
        self.finished_list = qtw.QListWidget()
        delete_button = qtw.QPushButton('Delete', clicked=lambda:self.remove_item_func())
        complete_button = qtw.QPushButton('Complete', clicked=lambda:self.finish_item_func())
        self.add_item = qtw.QLineEdit()
        add_button = qtw.QPushButton('Add Item', clicked=lambda:self.add_item_func(self.add_item.text()))

        self.to_do_list.setStyleSheet("background-color: white;")
        self.finished_list.setStyleSheet("background-color: white;")

        finished_label.setFont(qtg.QFont("Verdana",weight=qtg.QFont.Bold))
        to_do_label.setFont(qtg.QFont("Verdana",weight=qtg.QFont.Bold))

        delete_button.setStyleSheet("background-color: red; font-weight: bold; opacity: 50%;")
        complete_button.setStyleSheet("background-color: lightgreen; font-weight: bold; opacity: 50%;")

        self.add_item.setStyleSheet("background-color: white;")
        add_button.setStyleSheet("background-color: lightblue; font-weight: bold; opacity: 50%;")

        container.layout().addWidget(to_do_label, 0, 0, 1, 4)
        container.layout().addWidget(self.to_do_list, 1, 0, 4, 4)
        container.layout().addWidget(finished_label, 0, 4, 1, 4)
        container.layout().addWidget(self.finished_list, 1, 4, 4, 4)
        container.layout().addWidget(delete_button, 6, 2, 1, 1.5)
        container.layout().addWidget(complete_button, 6, 5, 1, 1.5)
        container.layout().addWidget(self.add_item, 7, 2, 1, 4)
        container.layout().addWidget(add_button, 8, 3, 1, 2)

        self.layout().addWidget(container)

    def add_item_func(self, item_):
        if len(item_) > 0:
            item_ = ' * ' + item_
            self.to_do_list.addItem(item_)
            self.add_item.setText('')
        else: return

    def remove_item_func(self):
        select_item = self.to_do_list.selectedItems()
        if not select_item: return
        for item in select_item: self.to_do_list.takeItem(self.to_do_list.row(item))

    def finish_item_func(self):
        select_item = self.to_do_list.selectedItems()
        if not select_item: return
        for item in select_item:
            self.finished_list.addItem(item.text())
            self.to_do_list.takeItem(self.to_do_list.row(item))

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
