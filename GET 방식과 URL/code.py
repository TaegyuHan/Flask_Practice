from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def login():
    username = request.args.get('user_name')
    passwd = request.args.get('pw')
    email = request.args.get('email')
    print(username, passwd, email)

    if username == "dave":
        return_data = {"auth": "success"}
    else:
        return_data = {"auth": "failed"}
    return jsonify(return_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

"""
    Rest API 이해를 위한 웹기술 이해: GET 방식과 URL
    완료
    
    Rest API 이해를 위한 웹기술 이해: GET 방식과 HTML > 시작  
"""