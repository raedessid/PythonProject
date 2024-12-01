# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
import bg_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(800, 600)
        dashboard.setStyleSheet(u"")
        self.label_2 = QLabel(dashboard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 260, 251, 101))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.analyse = QLabel(dashboard)
        self.analyse.setObjectName(u"analyse")
        self.analyse.setGeometry(QRect(380, 190, 91, 81))
        self.analyse.setPixmap(QPixmap(u":/photos/magnifying-glass (1).png"))
        self.label_7 = QLabel(dashboard)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(570, 300, 201, 20))
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_4 = QLabel(dashboard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 290, 151, 41))
        self.label_4.setFont(font1)
        self.traffic = QLabel(dashboard)
        self.traffic.setObjectName(u"traffic")
        self.traffic.setGeometry(QRect(610, 190, 131, 81))
        self.traffic.setPixmap(QPixmap(u":/photos/traffic.png"))
        self.Scan = QLabel(dashboard)
        self.Scan.setObjectName(u"Scan")
        self.Scan.setGeometry(QRect(110, 200, 71, 91))
        self.Scan.setPixmap(QPixmap(u":/photos/responsive (1).png"))

        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"Scan Devices/ports", None))
        self.analyse.setText("")
        self.label_7.setText(QCoreApplication.translate("dashboard", u"Traffic Monitoring", None))
        self.label_4.setText(QCoreApplication.translate("dashboard", u"ports analyses", None))
        self.traffic.setText("")
        self.Scan.setText("")
    # retranslateUi

