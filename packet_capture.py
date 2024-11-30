import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5 import uic
from scapy.all import sniff, get_if_list, conf  # For packet capture and interface list
from PyQt5.QtCore import QThread, pyqtSignal


# Define the worker thread to handle packet capture in the background
class CaptureThread(QThread):
    packet_captured = pyqtSignal(object)  # Signal to send captured packet data
    finished = pyqtSignal()  # Signal when capture finishes

    def __init__(self, network_interface):
        super().__init__()
        self.network_interface = network_interface
        self.running = True  # Flag to control sniffing

    def run(self):
        """Capture packets continuously in the background."""
        conf.sniff_promisc = True

        def packet_callback(packet):
            if self.running:  # Continue sniffing until the flag is set to False
                self.packet_captured.emit(packet)  # Emit signal for each captured packet

        try:
            # Sniff packets indefinitely
            sniff( prn=packet_callback, store=0)
        except Exception as e:
            print(f"Error in sniffing packets: {e}")
        finally:
            self.finished.emit()  # Emit finished signal when capture is done or stopped

    def stop_capture(self):
        """Stop packet capturing."""
        self.running = False  # Stop packet sniffing by changing the flag


class PacketCaptureApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI from the .ui file
        uic.loadUi("traffic_monitoring1.ui", self)

        # Connect buttons to methods
        self.pushButton_3.clicked.connect(self.start_capture)  # Start capture button
        self.pushButton_4.clicked.connect(self.stop_capture)   # Stop capture button

        # Initially, disable the stop button
        self.pushButton_4.setEnabled(False)

        # Define a list to hold the captured packet data
        self.packet_data = []

        # Set the network interface to sniff on (use a method to list available interfaces)
        self.network_interface = self.get_network_interface()

        # Set up the capture thread
        self.capture_thread = None

    def get_network_interface(self):
        """Return the first network interface available for sniffing."""
        interfaces = get_if_list()
        if interfaces:
            return interfaces[0]  # Use the first available network interface
        return None

    def start_capture(self):
        """Start capturing packets."""
        self.pushButton_3.setEnabled(False)  # Disable the start button during capture
        self.pushButton_4.setEnabled(True)   # Enable the stop button

        if self.capture_thread is None:
            # Initialize and start the capture thread
            self.capture_thread = CaptureThread(self.network_interface)
            self.capture_thread.packet_captured.connect(self.process_packet)
            self.capture_thread.finished.connect(self.on_capture_finished)
            self.capture_thread.start()

    def stop_capture(self):
        """Stop capturing packets."""
        self.pushButton_3.setEnabled(True)  # Enable the start button
        self.pushButton_4.setEnabled(False)  # Disable the stop button

        if self.capture_thread is not None:
            self.capture_thread.stop_capture()  # Stop the capture thread

    def on_capture_finished(self):
        """Handle capture thread finishing."""
        self.capture_thread.wait()  # Wait for the thread to finish
        self.capture_thread = None  # Reset the capture thread

    def process_packet(self, packet):
        """Process and display captured packet."""
        try:
            # Extract relevant packet information (source IP, destination IP, protocol, etc.)
            if packet.haslayer("IP"):
                source = packet["IP"].src
                destination = packet["IP"].dst
                protocol = packet["IP"].proto
                protocol_name = self.get_protocol_name(protocol)
                info = str(packet.summary())  # Info about the packet
                timestamp = time.ctime()  # Current time

                # Add the captured packet data to the list
                self.packet_data.append([source, destination, protocol_name, info, timestamp])

                # Update the table with the captured packet data
                self.update_table()
            elif packet.haslayer("ARP"):
                # Capture ARP packets as well
                source = packet["ARP"].psrc
                destination = packet["ARP"].pdst
                protocol_name = "ARP"
                info = str(packet.summary())  # Info about the packet
                timestamp = time.ctime()  # Current time

                # Add the captured packet data to the list
                self.packet_data.append([source, destination, protocol_name, info, timestamp])

                # Update the table with the captured packet data
                self.update_table()

        except Exception as e:
            # Handle any packets that don't have the expected layers (e.g., malformed packets)
            print(f"Error processing packet: {e}")

    def get_protocol_name(self, protocol_number):
        """Convert protocol number to a human-readable protocol name."""
        protocol_map = {
            1: "ICMP",
            6: "TCP",
            17: "UDP",
            58: "ICMPv6",
        }
        return protocol_map.get(protocol_number, "Unknown")

    def update_table(self):
        """Update the QTableWidget with packet data."""
        # Set the row count to match the number of packets
        self.tableWidget.setRowCount(len(self.packet_data))

        # Add data to the table
        for row, packet in enumerate(self.packet_data):
            source_item = QTableWidgetItem(packet[0])  # Source IP
            destination_item = QTableWidgetItem(packet[1])  # Destination IP
            protocol_item = QTableWidgetItem(packet[2])  # Protocol (TCP, UDP, ARP, etc.)
            info_item = QTableWidgetItem(packet[3])  # Info (HTTP request, DNS, etc.)
            timestamp_item = QTableWidgetItem(packet[4])  # Timestamp

            # Add items to the corresponding columns in the table
            self.tableWidget.setItem(row, 0, source_item)
            self.tableWidget.setItem(row, 1, destination_item)
            self.tableWidget.setItem(row, 2, protocol_item)
            self.tableWidget.setItem(row, 3, info_item)
            self.tableWidget.setItem(row, 4, timestamp_item)


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PacketCaptureApp()
    window.show()
    sys.exit(app.exec_())
