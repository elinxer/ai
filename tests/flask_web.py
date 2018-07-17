"""
web服务器框架初试

Elinx

"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POSt'])
def home():
    return '<h1>Home, Done!</h1>'


@app.route('/test', methods=['GET', 'POST'])
def test():
    return "test"


if __name__ == '__main__':
    app.run()
