from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window = QMainWindow()
    window.setWindowTitle('Hello world!')
    window.resize(500, 300)
    label = QLabel('Hello world')
    label.setAlignment(Qt.AlignCenter)
    window.setCentralWidget(label)
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)