# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'discovering1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import form2_rc

class Ui_discovring(object):
    def setupUi(self, discovring):
        if not discovring.objectName():
            discovring.setObjectName(u"discovring")
        discovring.resize(800, 600)
        self.pushButton = QPushButton(discovring)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 510, 141, 31))
        self.pushButton_2 = QPushButton(discovring)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(620, 510, 121, 31))
        self.label_2 = QLabel(discovring)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 130, 55, 16))
        self.label_3 = QLabel(discovring)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 130, 55, 16))
        self.label_4 = QLabel(discovring)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 150, 55, 16))
        self.label_5 = QLabel(discovring)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 150, 55, 16))
        self.label_12 = QLabel(discovring)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 170, 55, 16))
        self.label_61 = QLabel(discovring)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(130, 170, 55, 16))
        self.label_62 = QLabel(discovring)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(270, 170, 55, 16))
        self.label_63 = QLabel(discovring)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(210, 130, 55, 16))
        self.label_64 = QLabel(discovring)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(270, 150, 55, 16))
        self.label_65 = QLabel(discovring)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(210, 170, 55, 16))
        self.label_66 = QLabel(discovring)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(270, 130, 55, 16))
        self.label_67 = QLabel(discovring)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(210, 150, 55, 16))
        self.label_68 = QLabel(discovring)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(210, 30, 71, 91))
        self.label_68.setPixmap(QPixmap(u"../../Downloads/computer (2).png"))
        self.label = QLabel(discovring)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 71, 91))
        self.label.setPixmap(QPixmap(u"../../Downloads/computer (2).png"))

        self.retranslateUi(discovring)

        QMetaObject.connectSlotsByName(discovring)
    # setupUi

    def retranslateUi(self, discovring):
        discovring.setWindowTitle(QCoreApplication.translate("discovring", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("discovring", u"Start Discovering", None))
        self.pushButton_2.setText(QCoreApplication.translate("discovring", u"Stop Discovering", None))
        self.label_2.setText(QCoreApplication.translate("discovring", u"hostname:", None))
        self.label_3.setText(QCoreApplication.translate("discovring", u"..", None))
        self.label_4.setText(QCoreApplication.translate("discovring", u"IP:", None))
        self.label_5.setText(QCoreApplication.translate("discovring", u"..", None))
        self.label_12.setText(QCoreApplication.translate("discovring", u"MAC:", None))
        self.label_61.setText(QCoreApplication.translate("discovring", u"..", None))
        self.label_62.setText(QCoreApplication.translate("discovring", u"..", None))
        self.label_63.setText(QCoreApplication.translate("discovring", u"hostname:", None))
        self.label_64.setText(QCoreApplication.translate("discovring", u"..", None))
        self.label_65.setText(QCoreApplication.translate("discovring", u"MAC:", None))
        self.label_66.setText(QCoreApplication.translate("discovring", u"..", None))
        self.label_67.setText(QCoreApplication.translate("discovring", u"IP:", None))
        self.label_68.setText("")
        self.label.setText("")
    # retranslateUi

