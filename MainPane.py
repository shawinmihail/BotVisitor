# -*- coding: utf-8 -*-
from PyQt5 import Qt, QtWidgets
import sys
from EventsCore import EventsCore
from Browser import Browser
from time import sleep


class MainPane(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setFixedSize(800, 800)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.create_widgets()

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
            url = Qt.QUrl("http://vk.com/im?sel=265355677")
            url = Qt.QUrl("http://rbk.ru/")
            url = Qt.QUrl("http://google.com")
            self.browser.load(url)

        self.button1.clicked.connect(act)

    def create_button_2(self):
        self.button2 = QtWidgets.QPushButton("Button2")
        self.button2.setFixedSize(70, 30)

        def act():
            page = self.browser.page()
            main_frame = page.mainFrame()

            # elements = main_frame.findAllElements("*")
            # for element in elements:
            #     name = element.attribute("name")
            #     if not name == "":
            #         print(element.attribute("name"))

            input_query = main_frame.findFirstElement("input[name=q]")
            button_happy = main_frame.findFirstElement("input[name=btnI]")
            button_search = main_frame.findFirstElement("input[name='btnG']")

            input_query.setAttribute("value", "мясо")
            sleep(0.1)
            button_search.evaluateJavaScript("this.click()")

        self.button2.clicked.connect(act)



def start_app():
    app = QtWidgets.QApplication(sys.argv)
    main_pane = MainPane()
    main_pane.show()
    sys.exit(app.exec_())