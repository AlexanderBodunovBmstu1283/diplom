import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setFixedSize(600,900)  # запрещает изменять размер окна
        self.statusBar()

        self.tab1=QtGui.QTextEdit()
        self.tab2 = QtGui.QTextEdit()
        ##################################
        self.vBoxlayout1 = QtGui.QVBoxLayout()
        self.vBoxlayout2 = QtGui.QVBoxLayout()
        ##############
        self.TextInput1 = QtGui.QTextEdit()
        self.TextInput1.setFixedSize(550, 600)

        self.PushButton1=QtGui.QPushButton()
        self.PushButton1.setFixedSize(550, 50)

        self.TextOutput1 = QtGui.QTextEdit()
        self.TextOutput1.setFixedSize(550, 50)
        ##############
        self.PushButton2 = QtGui.QPushButton()
        self.PushButton2.setFixedSize(550, 50)

        self.TextInput2 = QtGui.QLineEdit()
        self.TextInput2.setFixedSize(550,20)

        self.TextOutput2 = QtGui.QTextEdit()
        self.TextOutput2.setFixedSize(550, 500)

        ##############
        self.vBoxlayout1.addWidget(self.TextInput1)
        self.vBoxlayout1.addWidget(self.PushButton1)
        self.vBoxlayout1.addWidget(self.TextOutput1)
        self.tab1.setLayout(self.vBoxlayout1)
        ##################################
        self.vBoxlayout2.addWidget(self.PushButton2)
        self.vBoxlayout2.addWidget(self.TextInput2)
        self.vBoxlayout2.addWidget(self.TextOutput2)
        self.tab2.setLayout(self.vBoxlayout2)
        ##################################
        self.tab_widget = QtGui.QTabWidget()
        self.h_layout = QtGui.QWidget()

        self.tab_widget.addTab(self.tab1, 'Распознавание')
        self.tab_widget.addTab(self.tab2, 'Обучение')
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.tab_widget)

        self.summary_box = QtGui.QVBoxLayout()  #
        self.summary_box.addLayout(self.hbox)
        self.h_layout.setLayout(self.summary_box)

        self.setCentralWidget(self.h_layout)
        menubar = self.menuBar()
        self.PushButton1.clicked.connect(self.on_click)

    def on_click(self,list_tags):
        input_poem=self.TextInput1.getText()
        tags=get_tags(input_poem)
        self.TextOutput1.setText(list_tags)





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


def get_tags(text):
    pass