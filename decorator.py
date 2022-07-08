"""
    - 함수 앞뒤에 기능을 추가해서 손쉽게 함수 활용할 수 있는 기법
    - Closure function을 활용

"""


# 다음 함수를 함 보자

import args as args
import kwargs as kwargs


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

# log_func()

# 함수로 실행하기
# decorated_func = outer_func(log_func)
# decorated_func()

# 이것을 한번에 데코레이터로 작성
@outer_func
def log_func():
    print("logging")

# 파라미터가 있는 데코레이터 부터 시작

"""
    flask 깊은 이해를 위한 파이썬 중급 문법: 파이썬 데코레이터1
    12분
    
    6분 52초0.0.
    
"""


def outer_func(function):
    def inner_func(digit1, digit2):
        if digit2 == 0:
            print("cannot be divided with zero")
            return
        function(digit1, digit2)
    return inner_func

# 데코레이터 사용하기 ( 유효성 검사 )
@outer_func
def divide(digit1, digit2):
    print(digit1 / digit2)

# divide(4, 2)
# divide(4, 0)


def type_checker(function):
    def inner_func(digit1, digit2):
        if (type(digit1) != int) or (type(digit2) != int):
            print("only integer support")
            return
        return function(digit1, digit2)
    return inner_func

@type_checker
def multiply(digit1, digit2):
    return digit1 * digit2

# multiply(1.1, 2)


"""
    여러개의 인자, 파라미터도 사용 가능하다.
"""
# 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들기
# 데코레이터 작성하기
def general_decorator(function):
    def wrapper(*args, **kwargs):
        print("function is decorated")
        return function(*args, **kwargs)
    return wrapper


# 데코레이터 적용하기
@general_decorator
def calc_square(digit):
    return digit * digit

@general_decorator
def calc_square(digit1, digit2):
    return digit1 + digit2

@general_decorator
def calc_square(digit1, digit2, digit3, digit4):
    return digit1 * digit2 * digit3 * digit4



"""
    한 함수에 데코레이터 2개 적용시키기
"""
# 여러 데코레이터 작성하기
def decorator1(function):
    def wrapper():
        print("decorator1")
        function()
    return wrapper

def decorator2(function):
    def wrapper():
        print("decorator2")
        function()
    return wrapper


@decorator1
@decorator2
def hello():
    print("hello")

# hello()

"""
   마크 보드, 이텔릭 만들어보기
"""
def mark_bold(function):
    def wrapper(*args, **kwargs):
        return "<b>" + function(*args, **kwargs) + "<b>"
    return wrapper


def mark_italic(function):
    def wrapper(*args, **kwargs):
        return "<i>" + function(*args, **kwargs) + "<i>"
    return wrapper


@mark_bold
@mark_italic
def add_html(string):
    return string

# print(add_html("안녕하세요"))


"""
   Method Decorator
   
   - 클래스의 method에도 데코레이터 적용 가능
"""
def h1_tag(funciton):
    def func_wrapper(self, *args, **kwargs):
        return f"<h1>{funciton(self, *args, **kwargs)}</h1>"
    return func_wrapper

# 클래스 선언시 메서드에 데코레이터 적용하기
class Person:
    def __init__(self,
                 first_name,
                 last_name):
        self.first_name = first_name
        self.last_name = last_name

    @h1_tag
    def get_name(self):
        return self.first_name + " " + self.first_name

# 데코레이터 적용 확인해보기
# davelee = Person("Lee", "Dave")
# print(davelee.get_name())


"""
    파라미터가 있는 Decorator 만들기 (심화)
    
    중첩 함수의 하나 더 깊게 두어 생성
"""
def decorator1(num):
    def outer_wrapper(function):
        def innter_wrapper(*args, **kwargs):
            print(f"decorator1: {num}")
            return function(*args, **kwargs)
        return innter_wrapper
    return outer_wrapper


def print_hello():
    print("hello")


# 위와 같이 작성하면, 다음과 같이 호출할 수 있다.
# print_hello2 = decorator1(1)(print_hello)
# print_hello2()

@decorator1(1)
def print_hello():
    print("hello")


@decorator1(num=2)
def print_hello():
    print("hello")

# print_hello()

"""
    HTML 데코레이터 만들어보기
"""
def mark_html(tag):
    def outer_wrapper(function):
        def innter_wrapper(*args, **kwargs):
            return f"<{tag}>{function(*args, **kwargs)}</{tag}>"
        return innter_wrapper
    return outer_wrapper

@mark_html("b")
def print_bold():
    return "hello"

@mark_html("h1")
def print_title(title):
    return title

print(print_bold())
print(print_title("잔재미코딩 Dave Lee 입니다."))