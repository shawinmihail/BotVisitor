# encoding: utf-8

if __name__ == '__main__':
    from PyQt5 import Qt, QtWidgets, QtCore
    enter_event = Qt.QKeyEvent(Qt.QEvent.KeyPress, Qt.Qt.Key_Enter, Qt.Qt.NoModifier)
    import MainPane
    MainPane.start_app()