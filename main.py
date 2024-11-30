import sys
import nmap
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from portscan import Ui_MainWindow  # Importer l'interface générée


# Fonction de scan des ports
def scan_ports(target_ip):
    scanner = nmap.PortScanner()
    try:
        scanner.scan(target_ip, '1-1024', '-sV')
        results = []
        if 'tcp' in scanner[target_ip]:
            for port in scanner[target_ip]['tcp']:
                state = scanner[target_ip]['tcp'][port]['state']
                service = scanner[target_ip]['tcp'][port]['name']
                product = scanner[target_ip]['tcp'][port].get('product', 'Unknown')
                version = scanner[target_ip]['tcp'][port].get('version', 'Unknown')
                results.append((port, service, f"{product} {version}"))
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []


# Classe principale de l'application
class PortScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connecter le tableau pour afficher les résultats
        self.ui.Portstable.setHorizontalHeaderLabels(["Port", "Service", "Details"])
        self.ui.Portstable.setColumnWidth(0, 100)
        self.ui.Portstable.setColumnWidth(1, 150)
        self.ui.Portstable.setColumnWidth(2, 200)

        # Exemple : Cible par défaut (vous pouvez ajouter une entrée utilisateur plus tard)
        target_ip = "127.0.0.1"

        # Déclencher le scan et afficher les résultats
        self.perform_scan(target_ip)

    def perform_scan(self, target_ip):
        results = scan_ports(target_ip)

        # Mise à jour des labels (exemple IP seulement ici)
        self.ui.contenuip.setText(target_ip)
        self.ui.contenuhostname.setText("sirine")
        self.ui.contenumac.setText("fffff")


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
