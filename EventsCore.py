# -*- coding: utf-8 -*-
from PyQt5 import Qt
import Signals
from time import sleep
from threading import Thread


class EventsCore:


    signal_send_evnt = Signals.SignalSendEvnt()

    @staticmethod
    def _send_click_event(point, release_delay):
        press = EventsCore._create_press_event(point)
        release = EventsCore._create_release_event(point)
        EventsCore.signal_send_evnt.emit(press)
        sleep(release_delay)
        EventsCore.signal_send_evnt.emit(release)

    @staticmethod
    def _create_press_event(point):
        press = Qt.QMouseEvent(Qt.QMouseEvent.MouseButtonPress, point, Qt.Qt.LeftButton, Qt.Qt.LeftButton, Qt.Qt.NoModifier)
        return press

    @staticmethod
    def _create_release_event(point):
        release = Qt.QMouseEvent(Qt.QMouseEvent.MouseButtonRelease, point, Qt.Qt.LeftButton, Qt.Qt.LeftButton, Qt.Qt.NoModifier)
        return release