# Form implementation generated from reading ui file 'C:\SeriesRobot\UpdateSeriesWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_updateSeriesWindow(object):
    def setupUi(self, updateSeriesWindow):
        updateSeriesWindow.setObjectName("updateSeriesWindow")
        updateSeriesWindow.resize(499, 440)
        updateSeriesWindow.setMinimumSize(QtCore.QSize(489, 376))
        self.gridLayout = QtWidgets.QGridLayout(updateSeriesWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(120, -1, 120, 15)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(updateSeriesWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(updateSeriesWindow)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(updateSeriesWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(updateSeriesWindow)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(updateSeriesWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(updateSeriesWindow)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(updateSeriesWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(updateSeriesWindow)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 62, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(updateSeriesWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(updateSeriesWindow)
        QtCore.QMetaObject.connectSlotsByName(updateSeriesWindow)

    def retranslateUi(self, updateSeriesWindow):
        _translate = QtCore.QCoreApplication.translate
        updateSeriesWindow.setWindowTitle(_translate("updateSeriesWindow", "Diziyi güncəllə"))
        self.label.setText(_translate("updateSeriesWindow", "Dizinin yeni adını daxil edin\n"
"(dəyişməmək üçün boş buraxın)"))
        self.lineEdit.setPlaceholderText(_translate("updateSeriesWindow", "Ad"))
        self.label_2.setText(_translate("updateSeriesWindow", "Dizinin yeni linkini daxil edin\n"
"(dəyişməmək üçün boş buraxın)"))
        self.lineEdit_2.setPlaceholderText(_translate("updateSeriesWindow", "Link"))
        self.label_3.setText(_translate("updateSeriesWindow", "Baxdığınız sonuncu sezonu daxil edin\n"
"(dəyişməmək üçün boş buraxın)"))
        self.lineEdit_3.setPlaceholderText(_translate("updateSeriesWindow", "Sezon"))
        self.label_4.setText(_translate("updateSeriesWindow", "Baxdığınız sonuncu bölümü daxil edin\n"
"(dəyişməmək üçün boş buraxın)"))
        self.lineEdit_4.setPlaceholderText(_translate("updateSeriesWindow", "Bölüm"))
        self.pushButton.setText(_translate("updateSeriesWindow", "Güncəllə"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updateSeriesWindow = QtWidgets.QWidget()
    ui = Ui_updateSeriesWindow()
    ui.setupUi(updateSeriesWindow)
    updateSeriesWindow.show()
    sys.exit(app.exec())
