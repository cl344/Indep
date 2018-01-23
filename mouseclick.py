# import sys
# from PyQt4 import QtGui, QtCore

# class Example(QtGui.QWidget):        
#     def __init__(self):
#         super(Example, self).__init__()            
#         self.initUI()

#     def mousePressEvent(self, QMouseEvent):
#         print QMouseEvent.pos()

#     def mouseReleaseEvent(self, QMouseEvent):
#         cursor =QtGui.QCursor()
#         print cursor.pos()        

#     def initUI(self):                           
#         qbtn = QtGui.QPushButton('Quit', self)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)       

#         self.setGeometry(0, 0, 1024, 768)
#         self.setWindowTitle('Quit button')    
#         self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
#         self.show()
#     def test(self):
#       print "test"

# def main():        
#     app = QtGui.QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

import sys

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, QLineEdit, QMessageBox




class DragButton(QtWidgets.QPushButton):

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)

def clicked():
    print ("click as normal!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(800,600)

    button = DragButton("Drag", w)
    button.clicked.connect(clicked)

    w.show()
    app.exec_()