# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'portscannew.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QWidget(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(-10, -30, 811, 641))
        self.background.setStyleSheet(u"QWidget{\n"
"background-color: black;\n"
"}")
        self.sideimage = QLabel(self.background)
        self.sideimage.setObjectName(u"sideimage")
        self.sideimage.setGeometry(QRect(-10, 0, 161, 621))
        self.sideimage.setPixmap(QPixmap(u"../image/cybersecurity.jpg"))
        self.sideimage.setScaledContents(True)
        self.frame = QFrame(self.background)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 60, 621, 201))
        self.frame.setStyleSheet(u"#frame{\n"
"    border: 2px solid #7084EA;\n"
"    border-radius: 10px;\n"
"    background-color: #F0F4FF;\n"
"    padding: 10px;\n"
" \n"
"}\n"
"#frame QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"\n"
"#frame QFormLayout {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frame:hover {\n"
"    border: 2px solid #5064CA; /* Darker shade on hover */\n"
"    background-color: #E8EBFF; /* Slightly darker background on hover */\n"
"}\n"
"#formLayout_6{\n"
"    background-color: transparent;\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.port_scanv = QLabel(self.frame)
        self.port_scanv.setObjectName(u"port_scanv")
        self.port_scanv.setGeometry(QRect(20, 10, 181, 41))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(10)
        font.setBold(True)
        self.port_scanv.setFont(font)
        self.port_scanv.setStyleSheet(u"QLabel {\n"
"    color: rgb(235, 52, 15)\n"
"}\n"
"#port_scanv{\n"
"background-color: transparent;\n"
"}")
        self.port_scanv.setWordWrap(True)
        self.imagehost = QLabel(self.frame)
        self.imagehost.setObjectName(u"imagehost")
        self.imagehost.setGeometry(QRect(0, 40, 161, 131))
        self.imagehost.setStyleSheet(u"#imagehost{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.imagehost.setPixmap(QPixmap(u"../../../../Downloads/computer-icon-transparent-free-png.webp"))
        self.imagehost.setScaledContents(True)
        self.Lhostname_6 = QLabel(self.frame)
        self.Lhostname_6.setObjectName(u"Lhostname_6")
        self.Lhostname_6.setGeometry(QRect(180, 70, 81, 16))
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        self.Lhostname_6.setFont(font1)
        self.Lhostname_6.setStyleSheet(u"QLabel{\n"
"rgb(56, 92, 133)\n"
"font-weight: bold;\n"
"font: 8pt \"Palatino Linotype\";\n"
"}")
        self.Lip_6 = QLabel(self.frame)
        self.Lip_6.setObjectName(u"Lip_6")
        self.Lip_6.setGeometry(QRect(180, 90, 81, 16))
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setBold(True)
        self.Lip_6.setFont(font2)
        self.Lip_6.setStyleSheet(u"QLabel{\n"
"rgb(56, 92, 133);\n"
"font-weight: bold;\n"
"font: 8pt \"Palatino Linotype\";\n"
"}")
        self.Lmac_6 = QLabel(self.frame)
        self.Lmac_6.setObjectName(u"Lmac_6")
        self.Lmac_6.setGeometry(QRect(180, 110, 91, 16))
        self.Lmac_6.setFont(font1)
        self.Lmac_6.setStyleSheet(u"QLabel{\n"
"rgb(56, 92, 133)\n"
"font-weight: bold;\n"
"font: 8pt \"Palatino Linotype\";\n"
"}")
        self.hosntameContainer = QLabel(self.frame)
        self.hosntameContainer.setObjectName(u"hosntameContainer")
        self.hosntameContainer.setGeometry(QRect(290, 70, 101, 16))
        font3 = QFont()
        font3.setFamilies([u"Palatino Linotype"])
        self.hosntameContainer.setFont(font3)
        self.maccontainer = QLabel(self.frame)
        self.maccontainer.setObjectName(u"maccontainer")
        self.maccontainer.setGeometry(QRect(290, 110, 91, 16))
        self.maccontainer.setFont(font3)
        self.ipcontainer = QLabel(self.frame)
        self.ipcontainer.setObjectName(u"ipcontainer")
        self.ipcontainer.setGeometry(QRect(290, 90, 101, 16))
        self.ipcontainer.setFont(font3)
        self.frame_2 = QFrame(self.background)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(170, 290, 621, 291))
        self.frame_2.setStyleSheet(u" #frame_2{\n"
"border: 2px solid #7084EA;\n"
"    border-radius: 10px;\n"
"    background-color: #F0F4FF;\n"
"    padding: 10px;\n"
"} \n"
"#frame_2 QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"\n"
"#frame_2 QFormLayout {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.activeportsv = QLabel(self.frame_2)
        self.activeportsv.setObjectName(u"activeportsv")
        self.activeportsv.setGeometry(QRect(20, 10, 101, 31))
        self.activeportsv.setFont(font)
        self.activeportsv.setStyleSheet(u"QLabel {\n"
"    color: rgb(235, 52, 15)\n"
"}")
        self.Portstable = QTableWidget(self.frame_2)
        if (self.Portstable.columnCount() < 3):
            self.Portstable.setColumnCount(3)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setForeground(brush);
        self.Portstable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.Portstable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.Portstable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Portstable.setObjectName(u"Portstable")
        self.Portstable.setGeometry(QRect(130, 30, 481, 241))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Portstable.sizePolicy().hasHeightForWidth())
        self.Portstable.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Palatino Linotype"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        self.Portstable.setFont(font4)
        self.Portstable.setMouseTracking(False)
        self.Portstable.setTabletTracking(False)
        self.Portstable.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Portstable.setAutoFillBackground(False)
        self.Portstable.setStyleSheet("""
#Portstable {
    background-color: #FFFFFF; /* Table body background */
    font: 75 8pt "Palatino Linotype";
}
QTableWidget::item {
    background-color: #FFFFFF; /* Cells background */
}
QHeaderView::section {
    background-color: #F0F4FF;
    color: black;
    font-weight: bold;
}
""")
        self.Portstable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Portstable.setAutoScroll(True)
        self.back = QPushButton(self.frame_2)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(20, 246, 81, 20))
        self.back.setStyleSheet(u"#back {\n"
"background-color: white;\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sideimage.setText("")
        self.port_scanv.setText(QCoreApplication.translate("MainWindow", u"Port scanning", None))
        self.imagehost.setText("")
        self.Lhostname_6.setText(QCoreApplication.translate("MainWindow", u"HOSTNAME", None))
        self.Lip_6.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.Lmac_6.setText(QCoreApplication.translate("MainWindow", u"MAC", None))
        self.hosntameContainer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.maccontainer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ipcontainer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.activeportsv.setText(QCoreApplication.translate("MainWindow", u"Active ports", None))
        ___qtablewidgetitem = self.Portstable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ports", None));
        ___qtablewidgetitem1 = self.Portstable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"services", None));
        ___qtablewidgetitem2 = self.Portstable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"vulnerability", None));
        self.back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
    # retranslateUi

