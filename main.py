import sys
import nmap
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Ui_newportscan import Ui_MainWindow  # Importer l'interface générée
from port_scanner import scan_ports  # Import the scan_ports function

# Classe principale de l'application
class PortScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

       #config tableau
        self.ui.Portstable.setHorizontalHeaderLabels(["Port", "Service", "Details"])
        self.ui.Portstable.setColumnWidth(0, 100)
        self.ui.Portstable.setColumnWidth(1, 150)
        self.ui.Portstable.setColumnWidth(2, 200)

        # Exemple de cible 
        target_ip = "127.0.0.1"

        # Déclencher le scan et afficher les résultats
        self.perform_scan(target_ip)

    def perform_scan(self, target_ip):
        
        results=scan_ports(target_ip)

        # Mise à jour des labels (exemple IP seulement ici)
        self.ui.ipcontainer.setText(target_ip)
        self.ui.hosntameContainer.setText("sirine")
        self.ui.maccontainer.setText("fffff")


        # Remplir le tableau avec les résultats
        self.ui.Portstable.setRowCount(len(results))
        for row, (port, service, details) in enumerate(results):
            self.ui.Portstable.setItem(row, 0, QTableWidgetItem(str(port)))
            self.ui.Portstable.setItem(row, 1, QTableWidgetItem(service))
            self.ui.Portstable.setItem(row, 2, QTableWidgetItem(details))


# Lancer l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PortScannerApp()
    window.show()
    sys.exit(app.exec())
