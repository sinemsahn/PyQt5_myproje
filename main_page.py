from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

import os
import socket  # for socket

from deneme_python import Ui_AnaPencere


class MainPage(QWidget):

    def __init__(self):

        super().__init__()

        self.ana=Ui_AnaPencere()
        self.ana.setupUi(self)



        self.setWindowTitle('Network')





        #signol slot bağlantısı
        self.ana.pingButton.clicked.connect(self.open_ping_page)
        self.ana.ipButton.clicked.connect(self.open_ip_page)
        self.ana.portButton.clicked.connect(self.open_nmap_open)
        self.ana.cancelButton.clicked.connect(self.exit_function)
    def exit_function(self):
        exec()


    def open_ip_page(self):
        adres=self.ana.ipkutu.text()


        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as err:
            self.ana.label_2.setText("Hata balant kurulamad.")

        # default port for socket
        port = 80

        try:
            host_ip = socket.gethostbyname(adres)
        except socket.gaierror:

            # this means could not resolve the host
            self.ana.label_2.setText("Hata!")


        # connecting to the server
        s.connect((host_ip, port))

        self.ana.label_2.setText(" port == %s host ismi== %s" % (host_ip, adres))









    def open_ping_page(self):
        new_name=self.ana.pingkutu.text()
        hostname = new_name  # example
        response = os.system("ping   " + hostname)

        # and then check the response...
        if response == 0:

            self.ana.label_2.setText(hostname+" up! ")



        else:
            self.ana.label_2.setText(hostname + " down! ")





    def open_nmap_open(self):
        new_nmap_port=self.ana.portkutu.text()
        port=self.ana.spinBox.text()


        self.deneme(new_nmap_port,port)

    def deneme(self, new_nmap_port, port):


        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


            port = int(port)


            client.connect((new_nmap_port, port))

            from_server = client.recv(4096)
            self.ana.port_label.setText("IP: "+str(new_nmap_port)+" PORT: "+str(port)+"  Hedef port ack.")


        except socket.error as err:
            self.ana.port_label.setText("IP: " + str(new_nmap_port) + " PORT: " + str(port) + "  Hedef port kapal." )






app=QApplication([])
window=MainPage()
window.show()
app.exec_()
