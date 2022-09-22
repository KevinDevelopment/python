# symmetric_server.py
import os
from flask import Flask
from cryptography.fernet import Fernet

SECRET_KEY = os.environb[b"SECRET_KEY"]
SECRET_MESSAGE = b"fluffy tail"
app = Flask(__name__)

my_cipher = Fernet(SECRET_KEY)


@app.route("/")
def get_secret_message():
    return my_cipher.encrypt(SECRET_MESSAGE)
# uwsgi --http-socket 127.0.0.1:5683 \
 #   --env SECRET_KEY="8jtTR9QcD-k3RO9Pcd5ePgmTu_itJQt9WKQPzqjrcoM=" \
  #  --mount /=symmetric_server:app
