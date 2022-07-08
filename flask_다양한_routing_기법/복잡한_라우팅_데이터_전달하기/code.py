from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello World!</h1>"


@app.route('/profile/<username>')
def get_profile(username):
    return f"profile: {username}"


@app.route('/first/<username>')
def get_first(username):
    return f"<h3>{username} !</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8080")