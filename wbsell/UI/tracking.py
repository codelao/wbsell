# Form implementation generated from reading ui file 'tracking.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 500)
        Dialog.setStyleSheet("")
        self.choiceFrame = QtWidgets.QFrame(parent=Dialog)
        self.choiceFrame.setGeometry(QtCore.QRect(30, 30, 261, 441))
        self.choiceFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.choiceFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.choiceFrame.setObjectName("choiceFrame")
        self.ordersButton = QtWidgets.QPushButton(parent=self.choiceFrame)
        self.ordersButton.setGeometry(QtCore.QRect(60, 50, 221, 43))
        self.ordersButton.setStyleSheet("")
        self.ordersButton.setObjectName("ordersButton")
        self.salesButton = QtWidgets.QPushButton(parent=self.choiceFrame)
        self.salesButton.setGeometry(QtCore.QRect(-20, 150, 231, 43))
        self.salesButton.setObjectName("salesButton")
        self.feedbacksButton = QtWidgets.QPushButton(parent=self.choiceFrame)
        self.feedbacksButton.setGeometry(QtCore.QRect(40, 250, 241, 43))
        self.feedbacksButton.setObjectName("feedbacksButton")
        self.questionsButton = QtWidgets.QPushButton(parent=self.choiceFrame)
        self.questionsButton.setGeometry(QtCore.QRect(-20, 350, 251, 43))
        self.questionsButton.setObjectName("questionsButton")
        self.outputFrame = QtWidgets.QFrame(parent=Dialog)
        self.outputFrame.setGeometry(QtCore.QRect(310, 50, 311, 421))
        self.outputFrame.setStyleSheet("")
        self.outputFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.outputFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.outputFrame.setObjectName("outputFrame")
        self.output = QtWidgets.QTextEdit(parent=self.outputFrame)
        self.output.setGeometry(QtCore.QRect(13, -3, 281, 421))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(330, -20, 271, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.resultLabel = QtWidgets.QLabel(parent=self.frame)
        self.resultLabel.setGeometry(QtCore.QRect(80, 30, 111, 31))
        self.resultLabel.setStyleSheet("")
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "wbsell • Отслеживание"))
        self.ordersButton.setText(_translate("Dialog", "Заказы за сегодня"))
        self.salesButton.setText(_translate("Dialog", "Продажи за сегодня"))
        self.feedbacksButton.setText(_translate("Dialog", "Неотвеченные отзывы"))
        self.questionsButton.setText(_translate("Dialog", "Неотвеченные вопросы"))
        self.output.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:15px;\"><br /></p></body></html>"))
        self.resultLabel.setText(_translate("Dialog", "Результат"))