# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import Qt


class SignalSendEvnt(QObject):

    signal = pyqtSignal(Qt.QMouseEvent)

    def emit(self, evnt):
        self.signal.emit(evnt)