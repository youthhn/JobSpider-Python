# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'job_spider.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_jobui(object):
    def setupUi(self, jobui):
        jobui.setObjectName("jobui")
        jobui.resize(640, 503)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        jobui.setWindowIcon(icon)
        jobui.setToolTipDuration(-1)
        self.label = QtWidgets.QLabel(jobui)
        self.label.setGeometry(QtCore.QRect(60, 110, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(jobui)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(jobui)
        self.label_3.setGeometry(QtCore.QRect(150, 220, 351, 201))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(jobui)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(jobui)
        self.pushButton.setGeometry(QtCore.QRect(460, 130, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(jobui)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 440, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(jobui)
        QtCore.QMetaObject.connectSlotsByName(jobui)

    def retranslateUi(self, jobui):
        _translate = QtCore.QCoreApplication.translate
        jobui.setWindowTitle(_translate("jobui", "招聘系统数据分析平台"))
        self.label.setText(_translate("jobui", "请输入关键词："))
        self.label_2.setText(_translate("jobui", "招聘系统数据分析平台 V1.0"))
        self.pushButton.setText(_translate("jobui", "立 即 分 析"))
        self.pushButton_2.setText(_translate("jobui", "点击查看报告"))

