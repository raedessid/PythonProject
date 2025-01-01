import sys
import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from scapy.all import *
from PyQt5.QtCore import QThread, pyqtSignal
from scapy.utils import wrpcap

class CaptureThread(QThread):
    packet_captured = pyqtSignal(object)
    finished = pyqtSignal()

    def __init__(self, network_interface, packet_type):
        super().__init__()
        self.network_interface = network_interface
        self.packet_type = packet_type
        self.running = False
        self.captured_packets = []

    def run(self):
        self.running = True
        conf.sniff_promisc = True

        def packet_callback(packet):
            if self.running:
                if self.packet_type == "All" or packet.haslayer(eval(self.packet_type)):
                    self.captured_packets.append(packet)
                    self.packet_captured.emit(packet)

        try:
            sniff(prn=packet_callback, store=0, stop_filter=lambda _: not self.running)
        except Exception as e:
            print(f"Error in sniffing packets: {e}")
        finally:
            self.running = False
            self.finished.emit()

    def stop_capture(self):
        self.running = False

class PacketCaptureApp(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("traffic_monitoring1.ui", self)

        self.pushButton_3.clicked.connect(self.start_capture)  # Start Capture
        self.pushButton_4.clicked.connect(self.stop_capture)  # Stop Capture
        self.pushButton.clicked.connect(self.download_packets)  # Download Packets
        self.pushButton_2.clicked.connect(self.close)  # Back Button
        self.pushButton_4.setEnabled(False)
        self.packet_data = []
        self.network_interface = self.get_network_interface()
        self.capture_thread = None

    def get_network_interface(self):
        interfaces = get_if_list()
        print(interfaces)
        if interfaces:
            return interfaces[0]
        return None

    def start_capture(self):
        selected_filter = self.packet_type.currentText()
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)

        if self.capture_thread is not None:
            self.stop_capture()

        self.packet_data = []
        self.update_table()

        if self.capture_thread is None:
            self.capture_thread = CaptureThread(self.network_interface, selected_filter)
            self.capture_thread.packet_captured.connect(self.process_packet)
            self.capture_thread.finished.connect(self.on_capture_finished)
            self.capture_thread.start()

    def stop_capture(self):
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(False)
        if self.capture_thread is not None:
            self.capture_thread.stop_capture()

    def on_capture_finished(self):
        if self.capture_thread:
            self.capture_thread.wait()
            self.capture_thread = None

    def process_packet(self, packet):
        try:
            if packet.haslayer(ARP):
                source_ip = packet[ARP].psrc
                destination_ip = packet[ARP].pdst
                source_mac = packet[ARP].hwsrc
                destination_mac = packet[ARP].hwdst
                protocol_name = "ARP"
                flags = "N/A"
                info = str(packet.summary())
                source_port = "N/A"
                destination_port = "N/A"
                timestamp = time.ctime()
                self.packet_data.append(
                    [source_ip, destination_ip, source_mac, destination_mac, protocol_name, flags, info, source_port,
                     destination_port, timestamp]
                )

            elif packet.haslayer(ICMP) and packet.haslayer(IP):
                source_ip = packet[IP].src
                destination_ip = packet[IP].dst
                source_mac = "N/A"
                destination_mac = "N/A"
                protocol_name = "ICMP"
                flags = "N/A"
                info = str(packet.summary())
                source_port = "N/A"
                destination_port = "N/A"
                timestamp = time.ctime()
                self.packet_data.append(
                    [source_ip, destination_ip, source_mac, destination_mac, protocol_name, flags, info, source_port,
                     destination_port, timestamp]
                )

            elif packet.haslayer(TCP) and packet.haslayer(IP):
                source_ip = packet[IP].src
                destination_ip = packet[IP].dst
                source_mac = "N/A"
                destination_mac = "N/A"
                protocol_name = "TCP"
                flags = str(packet[TCP].flags)  # Convert to string
                source_port = packet[TCP].sport
                destination_port = packet[TCP].dport
                info = f"{source_ip}:{source_port} -> {destination_ip}:{destination_port}"
                timestamp = time.ctime()
                self.packet_data.append(
                    [source_ip, destination_ip, source_mac, destination_mac, protocol_name, flags, info, source_port,
                     destination_port, timestamp]
                )

            elif packet.haslayer(UDP) and packet.haslayer(IP):
                source_ip = packet[IP].src
                destination_ip = packet[IP].dst
                source_mac = "N/A"
                destination_mac = "N/A"
                protocol_name = "UDP"
                flags = "N/A"
                source_port = packet[UDP].sport
                destination_port = packet[UDP].dport
                info = f"{source_ip}:{source_port} -> {destination_ip}:{destination_port}"
                timestamp = time.ctime()
                self.packet_data.append(
                    [source_ip, destination_ip, source_mac, destination_mac, protocol_name, flags, info, source_port,
                     destination_port, timestamp]
                )

            self.update_table()

        except Exception as e:
            print(f"Error processing packet: {e}")

    def update_table(self):
        self.tableWidget.setRowCount(len(self.packet_data))
        for row, packet in enumerate(self.packet_data):
            try:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(packet[0]))  # Source IP
                self.tableWidget.setItem(row, 1, QTableWidgetItem(packet[1]))  # Destination IP
                self.tableWidget.setItem(row, 2, QTableWidgetItem(packet[2]))  # Source MAC
                self.tableWidget.setItem(row, 3, QTableWidgetItem(packet[3]))  # Destination MAC
                self.tableWidget.setItem(row, 4, QTableWidgetItem(packet[4]))  # Protocol
                self.tableWidget.setItem(row, 5, QTableWidgetItem(packet[5]))  # Flags
                self.tableWidget.setItem(row, 6, QTableWidgetItem(packet[6]))  # Info
                self.tableWidget.setItem(row, 7, QTableWidgetItem(str(packet[7])))  # Source Port
                self.tableWidget.setItem(row, 8, QTableWidgetItem(str(packet[8])))  # Destination Port
                self.tableWidget.setItem(row, 9, QTableWidgetItem(packet[9]))  # Timestamp
            except Exception as e:
                print(f"Error updating row {row}: {e}")

    def download_packets(self):
        if self.packet_data:
            directory = os.path.expanduser(r"C:\Users\RaedE")
            file_path = os.path.join(directory, "packets.pcap")
            packets_to_save = self.capture_thread.captured_packets

            wrpcap(file_path, packets_to_save)
            QMessageBox.information(self, "Download Complete", f"Packets saved to {file_path}")

        else:
            QMessageBox.warning(self, "No Packets", "No packets captured to save.")


