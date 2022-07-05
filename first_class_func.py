"""
    - 데코레이터는 단지 파이썬 flask 뿐만 아니라, 다양한 언어 전반에 걸쳐서 많이 사용한다.
    - 파이썬 flask에서 나오는 데코레이터를 쓰기 전에, 언어 전반에 걸친 데코레이터 관련 기술을 이해 하기로 함
    - 한번 이해해 놓으면, 다양한 언어 전반에서 데코레이터를 만났을 떄마다 꾸준히 도움이 됨

    2. 중첩 함수 ( Nested function )
        - 함수 내부에 정의된 또다른 함수
        - 중첩함수는 해당 함수가 정의된 함수 내에서 호출 및 반환 가능
        - 함수 안에 선언된 변수는 함수 안에서만 사용 가능 한 원리와 동일 (로컬 변수)
"""


def outer_func():
    """ 와부 함수 """
    print("call outer_func function")

    # 중첩 함수의 정의
    def inner_func():
        """ 내부 함수 """
        return "call inner_func function"

    # 중첩 함수 호출
    print(inner_func())


# # 실행
# outer_func()


"""
    중첩 함수를 함수 밖에서도 호출할 수 있는 방법이 있다.
"""


def outer_func(num: int):
    """ 와부 함수 """

    # 중첩 함수 에서 외부 함수의 변수에 접근 가능
    def inner_func():
        """ 내부 함수 """
        print(num)
        return "complex"

    return inner_func


# # 실행
# fn = outer_func(10)
# print(fn())


"""
    First-class 함수
        - 다음과 같이 다룰 수 있는 함수를 First-class 함수라고 부름
            - 함수 자체를 변수에 저장 가능
            - 함수의 인자에 다른 함수를 인수로 전달 가능
            - 함수의 반환 값(return 값)으로 함수를 전달 가능  
"""


def calc_square(digit: int):
    return digit * digit


# print(calc_square(2))

func1 = calc_square


# print(func1(2))

# 활용
def calc_square(digit: int):
    return digit * digit


def calc_plus(digit: int):
    return digit + digit


def calc_quad(digit: int):
    return digit * digit * digit * digit


def list_square(function, digit_list):
    result = list()
    for digit in digit_list:
        result.append(function(digit))
    print(result)


num_list = [1, 2, 3, 4, 5]
# list_square(calc_square, num_list)
# list_square(calc_quad, num_list)
# list_square(calc_plus, num_list)

# 함수의 결과 값으로 함수를 리턴할 수 도 있음
def logger(msg):
    message = msg
    def msg_creater():
        print("[HIGH LEVEL]: ", message)
    return msg_creater

# log1 = logger("Dave Log-in")
# print(log1)
# log1()

def html_creator(tag):
    def text_wrapper(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return text_wrapper

# h1_html_creator = html_creator("h1")
# print(h1_html_creator)
# h1_html_creator("H1 태그는 타이틀을 표시하는 태그입니다.")
#
# p_html_creator = html_creator("p")
# p_html_creator("p 태그는 문단을 표시하는 태그입니다.")


def list_creator(tag):
    def text_wrapper(msg):
        print(f"{tag} {msg}")
    return text_wrapper

# data_list_minus = list_creator("-")
# data_list_minus("안녕")
#
# data_list_mul = list_creator("*")
# data_list_mul("안녕")
#
# data_list_x = list_creator("X")
# data_list_x("안녕")

"""
    Closure function
    - 함수와 해당 함수가 가지고 있는 데이터를 함께 복사, 저장해서 별도로 활용하는 기법으로 First-class 함수와 동일
    - 외부 함수가 소멸되더라도, 외부 함수 안에 있는 로컬 변수 값과 중첩함수 (내부함수)를 사용할 수 있는 기법
    - 지금까지 배운 언어의 맥락과는 뿌리가 다른 사고 - 함수형 프로그래밍에서 부터 고안된 기법
    - 그래서 처음에 접하면 매우 이해하기 어려움, 예제 코드로 보면서 이해하자.
"""

def outer_func(num):
    # 중첩 함수에서 외부 함수의 변수에 접근 가능
    def innder_func():
        print(num)
        return "안녕"
    return innder_func

closure_func = outer_func(10)
closure_func()

