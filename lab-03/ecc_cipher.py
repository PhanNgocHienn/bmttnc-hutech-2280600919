import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests



class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        
        try:
            # Send GET request to generate keys
            response = requests.get(url)

            if response.status_code == 200:
                # If successful, show the message
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        
        payload = {
            "message": self.ui.txt_info.toPlainText()  # Assuming txt_info is a text field to input the message
        }

        try:
            # Send POST request to sign the message
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                # If successful, display the signature
                data = response.json()
                self.ui.txt_sign.setText(data["signature"])  # Assuming txt_sign is a field to show the signature
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        
        payload = {
            "message": self.ui.txt_info.toPlainText(),  # Assuming txt_info is a text field to input the message
            "signature": self.ui.txt_sign.toPlainText()  # Assuming txt_sign is a text field containing the signature
        }

        try:
            # Send POST request to verify the signature
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                # If successful, check the verification result
                data = response.json()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                if data["is_verified"]:
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verification Failed")
                msg.exec_()
            else:
                print("Error while calling API")
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()  # Initialize the main window
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the event loop