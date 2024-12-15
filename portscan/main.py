import sys
import nmap
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from portscan import Ui_MainWindow  # Import the UI


# Scan ports using nmap
def scan_ports(target_ip):
    scanner = nmap.PortScanner()
    try:
        scanner.scan(target_ip, '1-1024', '-sV')  # Scan ports 1-1024
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
        print(f"Error during port scan: {e}")
        return []


# Main application class
class PortScannerApp(QMainWindow):
    def __init__(self, target_ip, hostname, mac_address):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up table headers
        self.ui.Portstable.setHorizontalHeaderLabels(["Port", "Service", "Details"])
        self.ui.Portstable.setColumnWidth(0, 100)
        self.ui.Portstable.setColumnWidth(1, 150)
        self.ui.Portstable.setColumnWidth(2, 300)

        # Display target information
        self.ui.contenuip.setText(target_ip)
        self.ui.contenuhostname.setText(hostname)
        self.ui.contenumac.setText(mac_address)

        # Perform and display the scan results
        self.perform_scan(target_ip)

    def perform_scan(self, target_ip):
        results = scan_ports(target_ip)

        # Clear table before updating
        self.ui.Portstable.setRowCount(0)

        # Populate table with scan results
        self.ui.Portstable.setRowCount(len(results))
        for row, (port, service, details) in enumerate(results):
            self.ui.Portstable.setItem(row, 0, QTableWidgetItem(str(port)))
            self.ui.Portstable.setItem(row, 1, QTableWidgetItem(service))
            self.ui.Portstable.setItem(row, 2, QTableWidgetItem(details))


# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: main.py <ip_address> <hostname> <mac_address>")
        sys.exit(1)

    # Read target information from arguments
    target_ip = sys.argv[1]
    hostname = sys.argv[2]
    mac_address = sys.argv[3]

    app = QApplication(sys.argv)
    window = PortScannerApp(target_ip, hostname, mac_address)
    window.show()
    sys.exit(app.exec())
