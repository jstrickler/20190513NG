#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_demo import Ui_Demo


class DemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Demo()
        self.ui.setupUi(self)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DemoMain()
    main.show()
    sys.exit(app.exec_())


