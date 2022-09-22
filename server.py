# server.py
from flask import Flask

SECRET_MESSAGE = "fluffy tail"
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE

# para rodar => uwsgi --http-socket 127.0.0.1:5683 --mount /=server:app http://localhost:5683
