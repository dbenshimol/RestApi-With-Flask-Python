from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Rest API is working!'


app.run(port=5000)