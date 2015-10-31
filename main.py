# encoding: utf-8
from PyQt5 import Qt, QtCore, QtWidgets, QtWebKit, QtWebKitWidgets, QtWebChannel, QtWebSockets, QtNetwork
import sys
from time import sleep


class Browser(QtWebKitWidgets.QWebView):

    def __init__(self):
        QtWebKitWidgets.QWebView.__init__(self)

        url = Qt.QUrl("http://vk.com/im?sel=265355677")
        url = Qt.QUrl("http://rbk.ru/")
        url = Qt.QUrl("http://google.com")
        self.load(url)
        page = self.page()
        element = page.mainFrame().findFirstElement("input[name=sfdiv]")
        element.setAttribute("value", "value")


app = QtWidgets.QApplication(sys.argv)
main_pane = Browser()
main_pane.show()
sys.exit(app.exec_())