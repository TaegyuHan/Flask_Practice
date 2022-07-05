"""
    - 함수 앞뒤에 기능을 추가해서 손쉽게 함수 활용할 수 있는 기법
    - Closure function을 활용

"""


# 다음 함수를 함 보자
def logger_login():
    print("Dave login")


# logger_login()

# 기능 추가
import datetime


def logger_login():
    """ 데이트 로그인 """
    print(datetime.datetime.now())
    print("Dave login")
    print(datetime.datetime.now())


# logger_login()

"""
    데코레이터 작성방법
"""


def datetime_decorater(func):
    def wrapper():
        print(f"time {datetime.datetime.now()}")
        func()
        print(datetime.datetime.now())

    return wrapper


# 데코레이터 적용하기
@datetime_decorater
def logger_login_david():
    print("David login")


# logger_login_david()


@datetime_decorater
def logger_login_tina():
    print("Tina login")


# logger_login_tina()


@datetime_decorater
def logger_login_anthony():
    print("Anthony login")


# logger_login_anthony()


# decorator 함수 정의
def outer_func(function):
    def inner_func():
        print("decoration added")
        function()
    return inner_func

# decorator할 함수
def log_func():
    print("logging")

log_func()

# 함수로 실행하기
decorated_func = outer_func(log_func)
decorated_func()

# 이것을 한번에 데코레이터로 작성
@outer_func
def log_func():
    print("logging")

# 파라미터가 있는 데코레이터 부터 시작

"""
    flask 깊은 이해를 위한 파이썬 중급 문법: 파이썬 데코레이터1
    12분
    
    6분 52초
"""


