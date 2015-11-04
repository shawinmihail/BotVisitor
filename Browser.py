# -*- coding: utf-8 -*-
from PyQt5 import QtWebKitWidgets
import C


class UserAgentWebPage(QtWebKitWidgets.QWebPage):

    def __init__(self):
        QtWebKitWidgets.QWebPage.__init__(self)

    def userAgentForUrl(self, QUrl):
        return(C.UserAgent.EXPLORER)


class Browser(QtWebKitWidgets.QWebView):

    def __init__(self):
        QtWebKitWidgets.QWebView.__init__(self)
        self.setPage(UserAgentWebPage())
