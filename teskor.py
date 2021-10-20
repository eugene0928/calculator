
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton

from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.value_1 = ""
        self.value_2 = ""
        self.operation = ""

        self.mainBox = QVBoxLayout()
        self.mainBox.setAlignment(Qt.AlignTop)
        self.setFixedSize(QSize(290, 200))

        # Background color
        self.setStyleSheet("background-color: #1C1C1C")

        # Box1
        self.Box1 = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setStyleSheet("background-color: white")
        self.Box1.addWidget(self.input)

        # Box2
        self.Box2 = QHBoxLayout()
        self.AC_button = QPushButton("AC")
        self.AC_button.setStyleSheet("background-color: #D4D4D3")

        self.percent_button = QPushButton("%")
        self.percent_button.setStyleSheet("background-color: #D4D4D3")

        self.divide_button = QPushButton("/")
        self.divide_button.setStyleSheet("background-color: #D4D4D3")

        self.backspace_button = QPushButton("<--")
        self.backspace_button.setStyleSheet("background-color: #FF9500")

        self.Box2.addWidget(self.AC_button)
        self.Box2.addWidget(self.percent_button)
        self.Box2.addWidget(self.divide_button)
        self.Box2.addWidget(self.backspace_button)

        # Box3

        self.Box3 = QHBoxLayout()
        self._7_button = QPushButton("7")
        self._7_button.setStyleSheet("background-color: #505050")

        self._8_button = QPushButton("8")
        self._8_button.setStyleSheet("background-color: #505050")

        self._9_button = QPushButton("9")
        self._9_button.setStyleSheet("background-color: #505050")

        self._x_button = QPushButton("*")
        self._x_button.setStyleSheet("background-color: #FF9500")

        self.Box3.addWidget(self._7_button)
        self.Box3.addWidget(self._8_button)
        self.Box3.addWidget(self._9_button)
        self.Box3.addWidget(self._x_button)

        # Box4

        self.Box4 = QHBoxLayout()
        self._4_button = QPushButton("4")
        self._4_button.setStyleSheet("background-color: #505050")

        self._5_button = QPushButton("5")
        self._5_button.setStyleSheet("background-color: #505050")

        self._6_button = QPushButton("6")
        self._6_button.setStyleSheet("background-color: #505050")

        self.minus_button = QPushButton("-")
        self.minus_button.setStyleSheet("background-color: #FF9500")

        self.Box4.addWidget(self._4_button)
        self.Box4.addWidget(self._5_button)
        self.Box4.addWidget(self._6_button)
        self.Box4.addWidget(self.minus_button)

        # Box5

        self.Box5 = QHBoxLayout()
        self._1_button = QPushButton("1")
        self._1_button.setStyleSheet("background-color: #505050")

        self._2_button = QPushButton("2")
        self._2_button.setStyleSheet("background-color: #505050")

        self._3_button = QPushButton("3")
        self._3_button.setStyleSheet("background-color: #505050")

        self.plus_button = QPushButton("+")
        self.plus_button.setStyleSheet("background-color: #FF9500")

        self.Box5.addWidget(self._1_button)
        self.Box5.addWidget(self._2_button)
        self.Box5.addWidget(self._3_button)
        self.Box5.addWidget(self.plus_button)

        # Box6

        self.Box6 = QHBoxLayout()
        self.zero_button = QPushButton("0")
        self.zero_button.setStyleSheet("background-color: #505050")

        self.dot_button = QPushButton(".")
        self.dot_button.setStyleSheet("background-color: #505050")

        self.exit_button = QPushButton("exit")
        self.exit_button.setStyleSheet("background-color: #505050")

        self.equal_button = QPushButton("=")
        self.equal_button.setStyleSheet("background-color: #FF9500")

        self.Box6.addWidget(self.zero_button)
        self.Box6.addWidget(self.dot_button)
        self.Box6.addWidget(self.exit_button)
        self.Box6.addWidget(self.equal_button)

        self.mainBox.addLayout(self.Box1)
        self.mainBox.addLayout(self.Box2)
        self.mainBox.addLayout(self.Box3)
        self.mainBox.addLayout(self.Box4)
        self.mainBox.addLayout(self.Box5)
        self.mainBox.addLayout(self.Box6)

        self.container = QWidget()
        self.container.setLayout(self.mainBox)

        self.setCentralWidget(self.container)

        self.zero_button.clicked.connect(lambda: self.number_clicked("0"))
        self._1_button.clicked.connect(lambda: self.number_clicked("1"))
        self._2_button.clicked.connect(lambda: self.number_clicked("2"))
        self._3_button.clicked.connect(lambda: self.number_clicked("3"))
        self._4_button.clicked.connect(lambda: self.number_clicked("4"))
        self._5_button.clicked.connect(lambda: self.number_clicked("5"))
        self._6_button.clicked.connect(lambda: self.number_clicked("6"))
        self._7_button.clicked.connect(lambda: self.number_clicked("7"))
        self._8_button.clicked.connect(lambda: self.number_clicked("8"))
        self._9_button.clicked.connect(lambda: self.number_clicked("9"))
        self.dot_button.clicked.connect(lambda: self.number_clicked("."))

        self.AC_button.clicked.connect(self.ac_clicked)

        self.exit_button.clicked.connect(self.exit_clicked)

        self.plus_button.clicked.connect(lambda: self.operation_chosen("+"))
        self.minus_button.clicked.connect(lambda: self.operation_chosen("-"))
        self.divide_button.clicked.connect(lambda: self.operation_chosen("/"))
        self._x_button.clicked.connect(lambda: self.operation_chosen("*"))
        self.percent_button.clicked.connect(lambda: self.operation_chosen("%"))
        self.equal_button.clicked.connect(self.get_result)

        self.backspace_button.clicked.connect(self.backspace)

    # slots

    def number_clicked(self, num: str) -> None:
        if not self.operation:
            self.value_1 += num
            self.input.setText(self.value_1)
        else:
            self.value_2 += num
            self.input.setText(self.value_2)

    def ac_clicked(self) -> None:
        self.value_1 = self.value_2 = self.operation = ""
        self.input.setText(self.value_1)

    @staticmethod
    def exit_clicked() -> None:
        sys.exit()

    def operation_chosen(self, operation: str) -> None:
        self.operation = operation
        self.value_2 = ""

    def get_result(self) -> None:
        if self.operation == "+":
            self.value_1 = str(float(self.value_1) + float(self.value_2))
            self.value_2 = self.operation = ""
            self.value1()
        elif self.operation == "-":
            self.value_1 = str(float(self.value_1) - float(self.value_2))
            self.value_2 = self.operation = ""
            self.value1()
        elif self.operation == "/":
            self.value_1 = str(float(self.value_1) / float(self.value_2))
            self.value_2 = self.operation = ""
            self.value1()
        elif self.operation == "*":
            self.value_1 = str(float(self.value_1) * float(self.value_2))
            self.value_2 = self.operation = ""
            self.value1()
        else:
            if self.value_1 and self.value_2 == "":
                self.value_1 = str(float(self.value_1) / 100)
                self.value_2 = self.operation = ""
                self.value1()
            else:
                error = "Malformed expression"
                self.input.setText(error)
                self.value_1 = self.value_2 = self.operation = ""

    def value1(self):
        if str(self.value_1).split(".")[-1] == "0":
            self.value_1 = self.value_1.split(".")[0]
        self.input.setText(self.value_1)

    def backspace(self):
        if self.value_1 and self.value_2 == "":
            numbers = list(self.value_1)
            numbers.pop(-1)
            self.value_1 = ''.join(numbers)
            self.input.setText(self.value_1)
        elif self.value_1 != "" and self.value_2 != "":
            numbers = list(self.value_2)
            numbers.pop(-1)
            self.value_2 = ''.join(numbers)
            self.input.setText(self.value_2)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()












