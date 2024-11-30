from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from discovering1 import Ui_discovring
from scapy.all import Ether, ARP, srp, IP, ICMP, sr1
import socket
import threading


class NetworkScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_discovring()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.startdisc.clicked.connect(self.start_scan)
        self.ui.stopdisc.clicked.connect(self.stop_scan)

        # Scanning state
        self.is_scanning = False

    def start_scan(self):
        """Start scanning the network."""
        self.is_scanning = True
        self.ui.tableWidget.setRowCount(0)  # Clear the table before scanning
        self.thread = threading.Thread(target=self.scan_network)
        self.thread.start()

    def stop_scan(self):
        """Stop scanning the network."""
        self.is_scanning = False

    def scan_network(self):
        """Perform the network scan."""
        network = "192.168.1.0/24"  # Adjust to your local network range

        try:
            for i in range(1, 255):  # Scanning 192.168.1.1 to 192.168.1.254
                if not self.is_scanning:
                    break

                ip = f"192.168.1.{i}"
                print(f"Scanning: {ip}")

                # Send ICMP request to check if host is alive
                response = sr1(IP(dst=ip)/ICMP(), verbose=False, timeout=1)
                if response and response.type == 0:  # Host is alive
                    mac = self.get_mac(ip)
                    hostname = self.get_hostname(ip)

                    # Update the table
                    self.add_host_to_table(ip, mac, hostname)

        except Exception as e:
            print(f"Error scanning network: {e}")

    def get_mac(self, ip):
        """Get the MAC address of a host."""
        try:
            frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
            response = srp(frame, timeout=2, verbose=False)[0]
            return response[0][1].hwsrc if response else "Unknown"
        except Exception:
            return "Unknown"

    def get_hostname(self, ip):
        """Get the hostname of a host."""
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"

    def add_host_to_table(self, ip, mac, hostname):
        """Add a host's details to the grid."""
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(ip))
        self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(mac))
        self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(hostname))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = NetworkScannerApp()
    window.show()
    sys.exit(app.exec())
