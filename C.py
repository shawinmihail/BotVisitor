# -*- coding: utf-8 -*-
from PyQt5 import Qt


class UserAgent:

    CHROME = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
    EXPLORER = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"


class Url:

    VK = Qt.QUrl("http://vk.com/im?sel=265355677")
    RBK = Qt.QUrl("http://rbk.ru/")
    GOOGLE = Qt.QUrl("http://google.com")
    YANDEX = Qt.QUrl("http://www.yandex.ru")