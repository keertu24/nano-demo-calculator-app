from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    return float(request.form['first'])+float(request.form['second'])

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return float(request.form['first'])+float(request.form['second'])

if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1')
