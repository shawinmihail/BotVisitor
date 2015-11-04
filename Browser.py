# -*- coding: utf-8 -*-
from PyQt5 import QtWebKitWidgets


class Browser(QtWebKitWidgets.QWebView):

    def __init__(self):
        QtWebKitWidgets.QWebView.__init__(self)