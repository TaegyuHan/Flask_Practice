from flask import Flask

app = Flask(__name__)


def add_file(data):
    return data + 5


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'


@app.route('/message/<int:message_id>')
def get_message(message_id):
    return f'get_message: {message_id}'


@app.route('/first/<int:message_id>')
def get_first(message_id):
    data = add_file(message_id)
    return f"<h1>{data}</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8080")