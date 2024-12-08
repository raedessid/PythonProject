import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from dashboard import Ui_dashboard
from network import NetworkScannerApp  b 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Dashboard UI setup
        self.dashboard_ui = Ui_dashboard()
        self.dashboard_widget = QWidget(self)
        self.dashboard_ui.setupUi(self.dashboard_widget)
        self.stacked_widget.addWidget(self.dashboard_widget)

        # NetworkScannerApp setup
        self.network_ui = NetworkScannerApp()  # Create instance of NetworkScannerApp
        self.stacked_widget.addWidget(self.network_ui)

        # Connect the button from the dashboard to switch to the network scanning screen
        self.dashboard_ui.Scan.mousePressEvent = self.move_to_discovering

    def move_to_discovering(self, event):
        # Switch to the network scanner widget
        self.stacked_widget.setCurrentWidget(self.network_ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
