import sys

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, QLineEdit, QMessageBox




class DragButton(QtWidgets.QLabel):

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

            #print (diff)


            newPos = self.mapFromGlobal(currPos + diff)
            # print("Qpoint")
            # print(newPos.x())
            # print(newPos.y())

            #print (type(newPos))
            dis = (newPos.x()-175)**2 + (newPos.y()-165)**2
            if dis<=5625:
                self.move(newPos)
                self.__mouseMovePos = globalPos
                print((newPos.x()-175),(newPos.y()-165))
            else:
                newPos.setX((newPos.x()-175)/(dis**0.5)*75+175)
                newPos.setY((newPos.y()-165)/(dis**0.5)*75+165)
                print((newPos.x()-175)/(dis**0.5)*75)
                print((newPos.y()-165)/(dis**0.5)*75)

                self.move(newPos)
                self.__mouseMovePos = globalPos
                #make the interpolation here

            # self.move(newPos)

            # self.__mouseMovePos = globalPos

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

    l1 = QtWidgets.QLabel(w)
    l1.setPixmap(QtGui.QPixmap('bg.png'))
    l1.move(100,90)


    button = DragButton(w)
    button.setPixmap(QtGui.QPixmap('thumb.png'))
    button.move(100+75,90+75)


    #button.clicked.connect(clicked)

    w.show()
    app.exec_()