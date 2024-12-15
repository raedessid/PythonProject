# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'portscan.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import hostimage_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.activeportsv = QLabel(self.centralwidget)
        self.activeportsv.setObjectName(u"activeportsv")
        self.activeportsv.setGeometry(QRect(10, 220, 101, 31))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(10)
        font.setBold(True)
        self.activeportsv.setFont(font)
        self.activeportsv.setStyleSheet(u"QLabel {\n"
"    color: red;\n"
"}")
        self.imagehost = QLabel(self.centralwidget)
        self.imagehost.setObjectName(u"imagehost")
        self.imagehost.setGeometry(QRect(10, 60, 161, 131))
        self.imagehost.setPixmap(QPixmap(u":/photo/467105502_1520897471899342_4847451542148929906_n.gif"))
        self.imagehost.setScaledContents(True)
        self.port_scanv = QLabel(self.centralwidget)
        self.port_scanv.setObjectName(u"port_scanv")
        self.port_scanv.setGeometry(QRect(10, 10, 181, 41))
        self.port_scanv.setFont(font)
        self.port_scanv.setStyleSheet(u"QLabel {\n"
"    color: red;\n"
"}")
        self.port_scanv.setWordWrap(True)
        self.Portstable = QTableWidget(self.centralwidget)
        if (self.Portstable.columnCount() < 3):
            self.Portstable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.Portstable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Portstable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Portstable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Portstable.setObjectName(u"Portstable")
        self.Portstable.setGeometry(QRect(160, 270, 451, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Portstable.sizePolicy().hasHeightForWidth())
        self.Portstable.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.Portstable.setFont(font1)
        self.Portstable.setMouseTracking(False)
        self.Portstable.setTabletTracking(False)
        self.Portstable.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Portstable.setAutoFillBackground(False)
        self.Portstable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Portstable.setAutoScroll(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 80, 281, 70))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Lhostname = QLabel(self.layoutWidget)
        self.Lhostname.setObjectName(u"Lhostname")
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setBold(True)
        self.Lhostname.setFont(font2)
        self.Lhostname.setStyleSheet(u"QLabel {\n"
"    color: rgb(85, 0, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Lhostname)

        self.contenuhostname = QLabel(self.layoutWidget)
        self.contenuhostname.setObjectName(u"contenuhostname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.contenuhostname)

        self.Lip = QLabel(self.layoutWidget)
        self.Lip.setObjectName(u"Lip")
        self.Lip.setFont(font2)
        self.Lip.setStyleSheet(u"QLabel {\n"
"    color: rgb(85, 0, 255);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Lip)

        self.contenuip = QLabel(self.layoutWidget)
        self.contenuip.setObjectName(u"contenuip")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.contenuip)

        self.Lmac = QLabel(self.layoutWidget)
        self.Lmac.setObjectName(u"Lmac")
        self.Lmac.setFont(font2)
        self.Lmac.setStyleSheet(u"QLabel {\n"
"    color: rgb(85, 0, 255);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Lmac)

        self.contenumac = QLabel(self.layoutWidget)
        self.contenumac.setObjectName(u"contenumac")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.contenumac)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.activeportsv.setText(QCoreApplication.translate("MainWindow", u"Active ports", None))
        self.imagehost.setText("")
        self.port_scanv.setText(QCoreApplication.translate("MainWindow", u"Port scanning", None))
        ___qtablewidgetitem = self.Portstable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ports", None));
        ___qtablewidgetitem1 = self.Portstable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"services", None));
        ___qtablewidgetitem2 = self.Portstable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"vulnerability", None));
        self.Lhostname.setText(QCoreApplication.translate("MainWindow", u"HOSTNAME:", None))
        self.contenuhostname.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Lip.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.contenuip.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Lmac.setText(QCoreApplication.translate("MainWindow", u"MAC:", None))
        self.contenumac.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

