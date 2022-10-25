import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolButton

class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(400,400,300,260)
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+D')  #shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget") #Tool tip
        self.closeButton.move(100,100)

class ToolButton(QMainWindow):

    def __init__(self):
        super(ToolButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ToolButton")
        self.setGeometry(400,400,300,260)

        self.toolbar = self.addToolBar("toolBar")
        self.statusBar()

        self._detailsbutton = QToolButton()                                     
        self._detailsbutton.setCheckable(True)                                  
        self._detailsbutton.setChecked(False)                                   
        self._detailsbutton.setArrowType(Qt.RightArrow)
        self._detailsbutton.setAutoRaise(True)
        #self._detailsbutton.setIcon(QIcon("test.jpg"))
        self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self._detailsbutton.clicked.connect(self.showDetail)
        self.toolbar.addWidget(self._detailsbutton)

    def showDetail(self):
        if self._detailsbutton.isChecked():
            self.statusBar().showMessage("Show Detail....")
        else:
            self.statusBar().showMessage("Close Detail....")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ToolButton()
    ex.show()
    sys.exit(app.exec_())