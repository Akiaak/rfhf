from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()

label_win = QLabel('Нажмите чтобы узанть победителя!')
label_num = QLabel('?')
button = QPushButton('Сгенерировать')

line = QVBoxLayout()
line.addWidget(label_win, alignment=Qt.AlignCenter)
line.addWidget(label_num, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)

main_win.setLayout(line)

def show_winner():
    number = randint(1,100)
    label_win.setText('Победитель:')
    label_num.setText(str(number))

button.clicked.connect(show_winner)
main_win.show()
app.exec()