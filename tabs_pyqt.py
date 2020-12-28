from PyQt4 import QtGui, QtCore
import sys

app = QtGui.QApplication(sys.argv)


class Tab_widget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.window= QtGui.QWidget()
        self.field = QtGui.QLineEdit("Hello")
        self.button1 = QtGui.QPushButton("Del")

        self.box = QtGui.QVBoxLayout()
        self.box.addWidget(self.field)
        self.box.addWidget(self.button1, 1, QtCore.Qt.AlignRight)

        self.frame = QtGui.QFrame()
        self.frame.setLayout(self.box)

        self.button2 = QtGui.QPushButton("OK")
        self.box2 = QtGui.QVBoxLayout()
        self.box2.addWidget(self.button2, )
        self.group = QtGui.QGroupBox()
        self.group.setLayout(self.box2)

        self.tab = QtGui.QTabWidget()
        self.tab.addTab(self.frame, "&Обучение")  # вкладки
        self.tab.addTab(self.group, "&Распознавание")

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.tab)

        self.window.setLayout(self.vbox)


tab_widget=Tab_widget()

tab_widget.show()
sys.exit(app.exec_())


