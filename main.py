import sys
from PyQt5.QtWidgets import QApplication
from packet_capture import PacketCaptureApp

def main():
    app = QApplication(sys.argv)
    window = PacketCaptureApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

