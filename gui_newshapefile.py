# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_newshapefile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 178)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.newShapefileLE = QtWidgets.QLineEdit(Dialog)
        self.newShapefileLE.setObjectName("newShapefileLE")
        self.gridLayout_2.addWidget(self.newShapefileLE, 0, 1, 1, 1)
        self.fieldForNameLE = QtWidgets.QLineEdit(Dialog)
        self.fieldForNameLE.setObjectName("fieldForNameLE")
        self.gridLayout_2.addWidget(self.fieldForNameLE, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.newShapefileBrowseTB = QtWidgets.QToolButton(Dialog)
        self.newShapefileBrowseTB.setObjectName("newShapefileBrowseTB")
        self.gridLayout_2.addWidget(self.newShapefileBrowseTB, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create shapefile"))
        self.label.setText(_translate("Dialog", "New shapefile:"))
        self.label_2.setText(_translate("Dialog", "Field for name:"))
        self.newShapefileBrowseTB.setText(_translate("Dialog", "..."))

