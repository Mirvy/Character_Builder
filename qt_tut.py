import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>PythonPyQt.com</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>QLabel2</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('Hint')
        label3.setPixmap(QPixmap("python.png"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://python.org'>Python.org</a>")
        label4.setAlignment(Qt.AlignCenter)
        label4.setToolTip('Python.org')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel Example')

    def linkHovered(self):
        print('Link hovered')

    def linkClicked(self):
        print('Link clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())