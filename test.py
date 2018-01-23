import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()

	l1 = QtWidgets.QLabel(w)
	l1.setText("Hellow World")
	#l2 = QtWidgets.QLabel(w)
	#l2.setPixmap(QtGui.QPixmap('img.jpg'))

	b = QtWidgets.QPushButton('Push Me')



	h_box = QtWidgets.QHBoxLayout()
	h_box.addStretch();
	h_box.addWidget(l1);
	h_box.addStretch();



	v_box = QtWidgets.QVBoxLayout()
	v_box.addWidget(b)
	v_box.addLayout(h_box)
	w.setLayout(v_box)



	w.setWindowTitle("Cheng's Window")
	w.setGeometry(100,100,300,200)

	#l1.move(100,20)
	#l2.move(100,90)

	w.show()
	sys.exit(app.exec_())

window()


