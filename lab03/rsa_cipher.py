import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGenerate.clicked.connect(self.call_api_gen_keys)
        self.ui.btnEn.clicked.connect(self.call_api_encrypt)
        self.ui.btnDe.clicked.connect(self.call_api_decrypt)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVeri.clicked.connect(self.call_api_verify)
    
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", data["message"])
            else:
                QMessageBox.critical(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txtPlainText.toPlainText(), 
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtCPText.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.critical(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txtCPText.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtPlainText.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.critical(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txtInfo.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtSign.setPlainText(data["signature"])
                QMessageBox.information(self, "Success", "Signed Successfully")
            else:
                QMessageBox.critical(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txtInfo.toPlainText(), 
            "signature": self.ui.txtSign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    QMessageBox.information(self, "Success", "Verified Successfully")
                else:
                    QMessageBox.information(self, "Success", "Verification Failed")
            else:
                QMessageBox.critical(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
