import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from random import randint

class MainWindow(qtw.QWidget):


    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        self.number = randint(1, 101)
        self.components()
        self.show()

    def components(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        label_1 = qtw.QLabel('Guess The Number 1 - 100!!!')
        label_1.setFont(qtg.QFont("Verdana",weight=qtg.QFont.Bold))
        self.line_guess = qtw.QLineEdit()
        self.guess_button = qtw.QPushButton('Guess', clicked=lambda:self.guess(int(self.line_guess.text())))
        self.progress_bar = qtw.QProgressBar()
        self.progress_bar.setMaximum(100)
        self.hot_label = qtw.QLabel('Close...')
        self.hot_label.setFont(qtg.QFont("Verdana",weight=qtg.QFont.Bold))


        container.layout().addWidget(label_1, 0, 0, 1, 3)
        container.layout().addWidget(self.line_guess, 1, 0, 1, 3)
        container.layout().addWidget(self.guess_button, 1, 3, 1, 1)
        container.layout().addWidget(self.progress_bar, 2, 0, 1, 4)
        container.layout().addWidget(self.hot_label, 3, 0, 1, 4)


        self.layout().addWidget(container)

    def guess(self, guessed_num):
        try:
            if self.number == guessed_num:
                self.progress_bar.setValue(100)
                self.line_guess.setText('You Won! The number was - ', self.number)
                self.line_guess.setReadOnly(True)
            elif guessed_num - self.number < 10 and guessed_num - self.number > -10:
                self.progress_bar.setValue(90)
            elif guessed_num - self.number < 20 and guessed_num - self.number > -20:
                self.progress_bar.setValue(80)
            elif guessed_num - self.number < 30 and guessed_num - self.number > -30:
                self.progress_bar.setValue(70)
            elif guessed_num - self.number < 40 and guessed_num - self.number > -40:
                self.progress_bar.setValue(60)
            elif guessed_num - self.number < 50 and guessed_num - self.number > -50:
                self.progress_bar.setValue(50)
            elif guessed_num - self.number < 60 and guessed_num - self.number > -60:
                self.progress_bar.setValue(40)
            elif guessed_num - self.number < 70 and guessed_num - self.number > -70:
                self.progress_bar.setValue(30)
            elif guessed_num - self.number < 80 and guessed_num - self.number > -80:
                self.progress_bar.setValue(20)
            elif guessed_num - self.number < 90 and guessed_num - self.number > -90:
                self.progress_bar.setValue(10)
            else:
                self.progress_bar.setValue(0)
        except:
            self.hot_label.setText('Please enter an integer from 1 to 100!')
            return


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
