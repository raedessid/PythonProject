# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLabel
from PySide6.QtCore import Qt
from dashboard import Ui_dashboard  # Assuming dashboard UI is in dashboard_ui.py
from discovering1 import Ui_discovring  # Assuming discovering UI is in discovering_ui.py

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create the stacked widget to hold multiple screens
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create the dashboard and discovering screens
        self.dashboard_ui = Ui_dashboard()
        self.discovering_ui = Ui_discovring()

        # Set up the dashboard and discovering pages
        self.dashboard_widget = QWidget(self)
        self.dashboard_ui.setupUi(self.dashboard_widget)
        self.stacked_widget.addWidget(self.dashboard_widget)

        self.discovering_widget = QWidget(self)
        self.discovering_ui.setupUi(self.discovering_widget)
        self.stacked_widget.addWidget(self.discovering_widget)

        # Add an event to label_2 (the "Scan" label)
        self.dashboard_ui.Scan.mousePressEvent = self.move_to_discovering

    def move_to_discovering(self, event):
        """Move to the discovering page and close the current form."""
        self.stacked_widget.setCurrentWidget(self.discovering_widget)
        self.dashboard_widget.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


