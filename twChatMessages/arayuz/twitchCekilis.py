import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from untitled import Ui_MainWindow
import socket
import random
import re

class App(QtWidgets.QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)  
        self.setWindowTitle("Twitch çekiliş uygulaması")  
        self.setWindowIcon(QtGui.QIcon('tw.png'))

        # Widget ayarları
        self.ui.pushButton.clicked.connect(self.getMessagesAndDrawUser)
        self.server = 'irc.chat.twitch.tv'
        self.port = 6667
        self.nickname = 'dyshoxx'
        self.token = 'oauth:flc4m7srva6woi8dhoxl2cnml7dbmi'
        self.sock = None
        self.is_connected = False  # Bağlantı kontrolü

        # Timer ayarları
        self.timer = QtCore.QTimer(self) 
        self.timer.timeout.connect(self.getMessages)
        
        # Mesaj ve kullanıcı listeleri
        self.listOfMessages = []
        self.listOfUsers = []
        self.listOfSelectedMessages = []
        self.listOfSelectedMessageOwners = []

        # görsellik için bir takım düzenlemeler
        self.ui.label.setStyleSheet("font-weight : bold ;font-size : 14px")
        self.ui.label_2.setStyleSheet("font-weight : bold ;font-size : 14px")
        self.ui.label_3.setStyleSheet("font-weight : bold ;font-size : 14px")
        self.ui.label_4.setStyleSheet("font-weight : italic,bold ;font-size : 40px;")
        self.ui.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.plainTextEdit.setStyleSheet("font-size : 24px")
        self.ui.plainTextEdit_2.setStyleSheet("font-size : 24px")
        self.ui.plainTextEdit_3.setStyleSheet("font-size : 24px")
        self.ui.pushButton.setStyleSheet("font-weight : bold ;font-size : 30px")
        self.ui.listWidget.setStyleSheet("font-weight : bold ;font-size : 26px")

    def getInputs(self):
        # Kullanıcıdan alınan girişler
        self.streamerName = "#" + self.ui.plainTextEdit.toPlainText()
        self.duration = int(self.ui.plainTextEdit_2.toPlainText()) * 1000  # milisaniye olarak süre
        self.word = self.ui.plainTextEdit_3.toPlainText()

    def connectToTwitch(self):
        if not self.is_connected:
            try:
                self.sock = socket.socket()
                self.sock.connect((self.server, self.port))

                self.sock.send(f"PASS {self.token}\n".encode('utf-8'))  # Şifre (OAuth token)
                self.sock.send(f"NICK {self.nickname}\n".encode('utf-8'))  # Kullanıcı adı
                self.sock.send(f"JOIN {self.streamerName}\n".encode('utf-8'))  # Kanala katıl
                self.is_connected = True
                print("Bağlantı başarılı.")
            except socket.error as e:
                print(f"Bağlantı hatası: {e}")

    def getMessages(self):
        try:
            response = self.sock.recv(2048).decode('utf-8')
            if response.startswith('PING'):
                self.sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
            elif "PRIVMSG" in response:
                user = response.split('!')[0][1:]  # Kullanıcı adı
                message = response.split('PRIVMSG')[1].split(':')[1].strip()  # Mesaj
                self.listOfMessages.append(message.lower())
                self.listOfUsers.append(user)

        except socket.error as e:
            print(f"Mesaj alma hatası: {e}")

    def getUsersByWord(self):
        # Kelimeye göre mesajları filtrele
        for message, user in zip(self.listOfMessages, self.listOfUsers):
            if re.search(rf"\b{self.word}\b", message):
                self.listOfSelectedMessages.append(message)
                self.listOfSelectedMessageOwners.append(user)

                self.ui.listWidget.addItem(user)
        

    def drawUser(self):
        if self.listOfSelectedMessageOwners:
            winnerUser = random.choice(self.listOfSelectedMessageOwners)
            self.ui.label_4.setText(winnerUser)
        else:
            self.ui.label_4.setText("Hiçbir kullanıcı\n çekilişe katılmadı.")

    def finishDraw(self):
        self.timer.stop()
        print("Çekiliş süresi doldu, kazanan belirleniyor...")
        self.getUsersByWord()  # Çekiliş kelimesine göre filtreleme
        self.drawUser()  # Kazananı belirleme

    def getMessagesAndDrawUser(self):
        self.ui.label_4.setText("DRAWİNG STARTED!")
        self.clearList()
        self.getInputs()  # Girişleri al
        self.connectToTwitch()  # Twitch'e bağlan
        self.listOfMessages.clear()
        self.listOfUsers.clear()
        self.listOfSelectedMessages.clear()
        self.listOfSelectedMessageOwners.clear()

        # Timer başlat, belirli süre boyunca mesajları al
        self.timer.start(1000)  # Her saniyede bir mesaj kontrol et
        QtCore.QTimer.singleShot(self.duration, self.finishDraw)  # Çekiliş süresi dolduğunda işlemi durdur

    def clearList(self):
        self.ui.listWidget.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    sys.exit(app.exec_())
