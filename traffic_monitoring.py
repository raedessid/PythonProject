# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'traffic_monitoring1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1215, 625)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 20, 361, 41))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(16)
        font.setWeight(QFont.)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(32, 54, 143);\n"
"font: 75 16pt \"Palatino Linotype\";")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(140, 460, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        font1.setItalic(True)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(0, 35, 51);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(280, 460, 121, 31))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 35, 51);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(140, 90, 1011, 341))
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setPointSize(9)
        font2.setWeight(QFont.)
        font2.setItalic(False)
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"font: 75 9pt \"Palatino Linotype\";\n"
"QTableWidget {\n"
"    border: 2px solid #7084EA;\n"
"    border-radius: 10px;\n"
"    background-color: #F0F4FF;\n"
"    padding: 10px;\n"
"}\n"
"QTableWidget:hover {\n"
"    border: 2px solid #5064CA;\n"
"    background-color: #E8EBFF;\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1000, 450, 141, 41))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 35, 51);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 10, 101, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 35, 51);")
        self.packet_type = QComboBox(Form)
        self.packet_type.addItem("")
        self.packet_type.addItem("")
        self.packet_type.addItem("")
        self.packet_type.setObjectName(u"packet_type")
        self.packet_type.setGeometry(QRect(20, 110, 101, 31))
        self.packet_type.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.flags = QComboBox(Form)
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.addItem("")
        self.flags.setObjectName(u"flags")
        self.flags.setGeometry(QRect(20, 160, 101, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Packet Capture", None))
        self.label.setText(QCoreApplication.translate("Form", u"Network Traffic Monitoring", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Start Capture", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Stop Capture", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Source IP", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Destination IP", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Source MAC", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Destination MAC", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Protocol", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"flags", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Info", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Sport", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Dport", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Timestamp", None));
        self.pushButton.setText(QCoreApplication.translate("Form", u"Download Packets", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Back", None))
        self.packet_type.setItemText(0, QCoreApplication.translate("Form", u"TCP ", None))
        self.packet_type.setItemText(1, QCoreApplication.translate("Form", u"ARP", None))
        self.packet_type.setItemText(2, QCoreApplication.translate("Form", u"ICMP ", None))

        self.flags.setItemText(0, QCoreApplication.translate("Form", u"URG", None))
        self.flags.setItemText(1, QCoreApplication.translate("Form", u"ACK", None))
        self.flags.setItemText(2, QCoreApplication.translate("Form", u"PSH", None))
        self.flags.setItemText(3, QCoreApplication.translate("Form", u"RST", None))
        self.flags.setItemText(4, QCoreApplication.translate("Form", u"SYN", None))
        self.flags.setItemText(5, QCoreApplication.translate("Form", u"FIN", None))
        self.flags.setItemText(6, QCoreApplication.translate("Form", u"ECE", None))
        self.flags.setItemText(7, QCoreApplication.translate("Form", u"CWR", None))
        self.flags.setItemText(8, QCoreApplication.translate("Form", u"NS", None))

    # retranslateUi

