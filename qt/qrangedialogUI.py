# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qrangedialog.ui'
#
# Created: Sun Feb  9 13:11:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qrange(object):
    def setupUi(self, qrange):
        qrange.setObjectName("qrange")
        qrange.setWindowModality(QtCore.Qt.ApplicationModal)
        qrange.resize(348, 156)
        qrange.setModal(True)
        self.gridLayout = QtGui.QGridLayout(qrange)
        self.gridLayout.setObjectName("gridLayout")
        self.qmin = QtGui.QDoubleSpinBox(qrange)
        self.qmin.setSuffix("")
        self.qmin.setDecimals(4)
        self.qmin.setSingleStep(0.0001)
        self.qmin.setObjectName("qmin")
        self.gridLayout.addWidget(self.qmin, 0, 0, 1, 1)
        self.qmax = QtGui.QDoubleSpinBox(qrange)
        self.qmax.setDecimals(4)
        self.qmax.setSingleStep(0.0001)
        self.qmax.setObjectName("qmax")
        self.gridLayout.addWidget(self.qmax, 1, 0, 1, 1)
        self.numpnts = QtGui.QSpinBox(qrange)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numpnts.sizePolicy().hasHeightForWidth())
        self.numpnts.setSizePolicy(sizePolicy)
        self.numpnts.setWrapping(False)
        self.numpnts.setFrame(True)
        self.numpnts.setSpecialValueText("")
        self.numpnts.setMinimum(1)
        self.numpnts.setMaximum(100000)
        self.numpnts.setProperty("value", 1000)
        self.numpnts.setObjectName("numpnts")
        self.gridLayout.addWidget(self.numpnts, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(qrange)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(qrange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), qrange.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), qrange.reject)
        QtCore.QMetaObject.connectSlotsByName(qrange)

    def retranslateUi(self, qrange):
        qrange.setWindowTitle(QtGui.QApplication.translate("qrange", "Set Q range", None, QtGui.QApplication.UnicodeUTF8))
