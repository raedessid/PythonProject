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

        self.ui.startdisc.clicked.connect(self.start_scan)
        self.ui.stopdisc.clicked.connect(self.stop_scan)

        self.is_scanning = False

    def start_scan(self):
        self.is_scanning = True
        self.ui.tableWidget.setRowCount(0)
        self.thread = threading.Thread(target=self.scan_network)
        self.thread.start()

    def stop_scan(self):
        self.is_scanning = False

    def get_local_network(self):
        """Retrieve the local IP address and determine the network range."""
        try:
            # Open a dummy socket connection to determine the local IP
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                # Connect to a public IP (Google's public DNS server, not actually sending data)
                s.connect(("8.8.8.8", 80))
                local_ip = s.getsockname()[0]

            # Assume a default subnet mask of 255.255.255.0 (/24)
            network = '.'.join(local_ip.split('.')[:3]) + ".0/24"
            return network
        except Exception as e:
            print(f"Error detecting local network: {e}")
            return None

    def scan_network(self):
        network = self.get_local_network()
        if not network:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Error"))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Cannot detect local network"))
            return

        try:
            for i in range(1, 255):
                if not self.is_scanning:
                    break

                ip = f"{network.rsplit('.', 1)[0]}.{i}"
                print(f"Scanning: {ip}")

                response = sr1(IP(dst=ip) / ICMP(), verbose=False, timeout=1)
                if response and response.type == 0:
                    mac = self.get_mac(ip)
                    hostname = self.get_hostname(ip)
                    self.add_host_to_table(ip, mac, hostname)

        except Exception as e:
            print(f"Error scanning network: {e}")

    def get_mac(self, ip):
        try:
            frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
            response = srp(frame, timeout=2, verbose=False)[0]
            return response[0][1].hwsrc if response else "Unknown"
        except Exception:
            return "Unknown"

    def get_hostname(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"

    def add_host_to_table(self, ip, mac, hostname):
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
