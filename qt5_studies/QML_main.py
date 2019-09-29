# #!/usr/bin/python3
#
# import os, sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtQuick import *
# from PyQt5.Qt import *
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     engine = QQmlApplicationEngine()
#
#     engine.load(QUrl.fromLocalFile("main.qml"))
#
#     sys.exit(app.exec_())

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlComponent, QQmlApplicationEngine

# Create the application instance.
app = QGuiApplication(sys.argv)

# Create a QML engine.
engine = QQmlApplicationEngine()

# Create a component factory and load the QML script.
component = QQmlComponent(engine)
component.loadUrl(QUrl('main.qml'))

# Create the objects from the QML
window = component.create()
window.show()

sys.exit(app.exec_())
