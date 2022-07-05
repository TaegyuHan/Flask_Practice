from flask import Flask


app = Flask(__name__)  # Flask 객체를 app에 할당

"""
    __name__
    
    - __name__ 이라는 변수는 모듈의 이름이 저장됨
    - 실행하는 코드에서 __main__ 값이 들어감
"""


"""
   라우팅 (route) 이란?
   - 적절한 목적지를 찾아주는 기능
   - URL 을 해당 URL에 맞는 기능과 연결해줌
"""

# @ 데코레이터
@app.route("/hello")  # < 라우팅 경로
def hello():
    return "<h1>Hellow World!</h1>"


"""
    메인 모듈로 실행될 때 flask 웹 서버 구동
    
    - 서버로 구동한 IP와 포트를 옵셕ㄴ으로 넣어줄 수 있음
    - app.run() 함수로 서버 구동 가능
        - host, port, debug를 주로 사용함
        
            - host : 웹 주소
            - port : 포트
            - debug : True or False
"""

host_addr = "127.0.0.1"
port_num = "8080"

if __name__ == '__main__':
    app.run(
        host=host_addr,
        port=port_num,
        debug=False
    )
