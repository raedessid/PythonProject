from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QWidget
from PySide6.QtCore import QRect, QMetaObject


class Ui_discovring(object):
    def setupUi(self, discovring):
        discovring.setObjectName("discovring")
        discovring.resize(800, 600)

        self.startdisc = QPushButton(discovring)
        self.startdisc.setObjectName("startdisc")
        self.startdisc.setGeometry(QRect(460, 510, 141, 31))

        self.stopdisc = QPushButton(discovring)
        self.stopdisc.setObjectName("stopdisc")
        self.stopdisc.setGeometry(QRect(620, 510, 121, 31))

        self.tableWidget = QTableWidget(discovring)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(50, 50, 700, 400))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["IP Address", "MAC Address", "Hostname"])

        self.retranslateUi(discovring)
        QMetaObject.connectSlotsByName(discovring)

    def retranslateUi(self, discovring):
        discovring.setWindowTitle("Network Scanner")
        self.startdisc.setText("Start Discovering")
        self.stopdisc.setText("Stop Discovering")
