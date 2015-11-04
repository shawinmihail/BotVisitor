# -*- coding: utf-8 -*-
from PyQt5 import Qt, QtWidgets, QtCore
import sys
from EventsCore import EventsCore
from Browser import Browser
from time import sleep
import C


class MainPane(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setFixedSize(1000, 1000)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.create_widgets()
        self.do_visit()

        self.timer = QtCore.QTimer()
        self.timer.singleShot(3000, self.func)

    def do_visit(self):
        self.browser.load(C.Url.GOOGLE)

    def func(self):
        page = self.browser.page()
        main_frame = page.mainFrame()

        # elements = main_frame.findAllElements("*")
        # for element in elements:
        #     name = element.attribute("name")
        #     if not name == "":
        #         print(element.attribute("name"))

        input_query = main_frame.findFirstElement("input[name=q]")
        input_luck = main_frame.findFirstElement("input[name=btnI]")
        input_search = main_frame.findFirstElement("input[name=btnK]")

        input_query.evaluateJavaScript("this.focus()")
        input_query.setAttribute("value", "fresh meat")
        self.browser.event(Qt.QKeyEvent(Qt.QEvent.KeyPress, Qt.Qt.Key_Enter, Qt.Qt.NoModifier))
        sleep(50)
        references = main_frame.findFirstElement("href")
        print(references)


        # input_query.setFocus()
        # print(input_query.hasFocus())
        # input_query.setFocus()
        # print(input_query.hasFocus())
        # input_query.evaluateJavaScript("this.click()")

    def create_widgets(self):
        self.browser = Browser()
        self.create_butonn_1()
        self.create_button_2()

        self.layout.addWidget(self.browser, 1, 1)
        self.layout.addWidget(self.button1, 2, 1)
        self.layout.addWidget(self.button2, 2, 2)

    def create_butonn_1(self):
        self.button1 = QtWidgets.QPushButton("Button1")
        self.button1.setFixedSize(70, 30)

        def act():
            pass

        self.button1.clicked.connect(act)

    def create_button_2(self):
        self.button2 = QtWidgets.QPushButton("Button2")
        self.button2.setFixedSize(70, 30)
        self.button2.clicked.connect(self.func)


def start_app():
    app = QtWidgets.QApplication(sys.argv)
    main_pane = MainPane()
    main_pane.show()
    sys.exit(app.exec_())