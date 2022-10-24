import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    layout = QHBoxLayout()
    btn = QPushButton("Hello World!")
    layout.addWidget(btn)
    w.setLayout(layout)

    w.resize(500,500)
    w.move(100,100)
    w.setWindowTitle("Character Builder")
    w.setWindowIcon(QtGui.QIcon('icon.png'))
    w.show()
    sys.exit(app.exec_())