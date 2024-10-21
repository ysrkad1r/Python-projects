from PyQt5 import QtWidgets, QtCore
from ytArayuz import Ui_MainWindow
import random
import re
import sys
import requests
import time
from dateutil import parser

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Youtube çekiliş uygulaması")
        self.ui.pushButton.clicked.connect(self.mainFunc)

        # Stil etiketleri
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

        # Gerekli bilgiler
        self.apiKey = "AIzaSyDse5G-hj5NxYwBfuhy8SLnUYWLsbGNPoA"
        self.time = 0
        
        # Timer ayarları
        self.timer = QtCore.QTimer(self) 
        self.timer.timeout.connect(self.getMessagesFromChat)

        # Gerekli listeler
        self.messages = []
        self.users = []
        self.selectedUsers = []

    def getStreamId(self):
        self.videoUrl = self.ui.plainTextEdit.toPlainText()
        self.videoId = self.videoUrl.split("=")[1]
        
        self.videoUrlForFetching = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={self.videoId}&key={self.apiKey}" 
        self.response = requests.get(self.videoUrlForFetching).json()

        self.liveChatId = self.response['items'][0]['liveStreamingDetails']['activeLiveChatId']

    def requestMessagesFromChat(self):
        self.chatUrl = f"https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId={self.liveChatId}&part=snippet,authorDetails&key={self.apiKey}"
        self.chatResponse = requests.get(self.chatUrl).json()

        return self.chatResponse

    def getMessagesFromChat(self):
        self.chatResponse = self.requestMessagesFromChat()
        self.current_time = time.time()

        for item in self.chatResponse.get('items', []):
            self.user = item['authorDetails']['displayName']
            self.message = item['snippet'].get('displayMessage')
            timestamp = item['snippet']['publishedAt']

            # Zaman damgasını dateutil.parser ile işleme
            message_time = parser.isoparse(timestamp).timestamp()

            # Eğer mesaj son 10 saniye içindeyse ekle
            if self.current_time - message_time <= int(self.ui.plainTextEdit_2.toPlainText()):
                if self.message:
                    self.users.append(self.user)
                    self.messages.append(self.message)

    def controlOfWord(self):
        self.word = self.ui.plainTextEdit_3.toPlainText().lower()
        for message in self.messages:
            if re.search(rf"\b{self.word}\b", message.lower()):
                self.selectedUsers.append(self.users[self.messages.index(message)])
        
        return self.selectedUsers

    def finishDraw(self):
        self.timer.stop()
        self.controlOfWord()

        if not self.users:
            self.ui.label_4.setText("Hiç mesaj yok.")

        for user in self.selectedUsers:
            if user not in self.getAllItemsFromWidget():
                self.ui.listWidget.addItem(user)

        if self.selectedUsers:
            self.winnerUser = random.choice(self.selectedUsers)
            self.ui.label_4.setText(self.winnerUser)
        else:
            self.ui.label_4.setText("Bu kelimeyi içeren mesaj yok.")


    def getAllItemsFromWidget(self):
        self.items = []
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            if item is not None:
                self.items.append(item.text())
        return self.items


    def mainFunc(self):
        self.getStreamId()
        self.timer.start(1000)  # Her saniyede bir mesaj kontrol et
        QtCore.QTimer.singleShot(int(self.ui.plainTextEdit_2.toPlainText()) * 1000, self.finishDraw)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    window = App()  
    window.show()  
    sys.exit(app.exec_())
