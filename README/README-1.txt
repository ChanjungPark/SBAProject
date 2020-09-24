Object = 기능(function) + 속성(Property, Attribute, Feature) => 파라미터( AI 파트 )
하나의 { ... } 에 같이 있음
() 라운드 {} 컬 [] 스퀘어 브레이스 는 총 3가지 (전 프로그래밍 공통)
() 컨티션, 파라미터존, 튜플
{} 블락, JSON, Dict
[] array, 
[[]] matrix
===> notation 이라 합니다.
===> 언어기호학 
기본적으로 컴공 0, 1 만이 존재합니다. 이진수 binary code
위키 Geoge Bool 이란 사람 검색...
T, F 판단 1850년 --> 전선 (모스부호) --> 컴퓨터
선택지는 항상 두가지 중에 하나를 선택하는 구조 -> 컴공 해법
on, off 의 개념이다.
요소가 존재, 비존재 로 종류가 나뉜다. => Decision Tree (Origin AI 알고리즘)
Q 객체지향 vs 함수형 프로그래밍 를 구분하는 기준은
무엇이 있고 없고 인가 ?
A ... 속성이 있으면 객체지향, 없으면 함수형 프로그래밍
class Calculator:
    def __init__(self, num1, num2):  
    # 생성자 함수 --> 인스턴스(객체) 만드는 함수 __ 언더스코어 라고 합니다. 2개를 사용. 접근제한 private
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        return self.num1 + self.num2 
if __name__ == '__main__':
    calc = Calculator(6, 2)  # num1 = 6, num2 = 2
    sumResult = calc.sum()
    print(f'덧셈결과 {sumResult}')
    # 덧셈결과 : 8
    # 뺄셈결과 : 4
    # 곱셈결과 : 12
    # 나눗셈결과 : 3
결론: 객체지향은 속성이 존재해야 한다. 그리고 속성을 정의하는 곳은 __init__(속성파라미터) 이다.
self 는 객체내부의 속성에 접근하는 키워드
속성은 은닉화때문에 반드시 self. 로만 접근할 수 있다.
이는 보안의 기본처리이다. __init__은 클래스 내부에서만 접근한다.
클래스 내부에서 메소드의 종류는 몇가지인가 ? dynamic 동적 , static 정적
해석: 
기준: self 입니다
self exist dynamic -> 데이터를 메모리에서 메소드가 유효한 시간동안만 존재. 그 메소드가 소멸된 후 값은 self 에 저장된다
self !exist static -> 반 영속적으로 저장됨.
def print_info(self):
        print(f'이름 : {self.name}, 전화번호: {self.phone}, 이메일: {self.email}, 주소: {self.addr}') 
        # self.name 과  name 은 서로 다른 존재이므로 {self.name} 과 {name} 은 서로 다른 상태이다.
@staticmethod
def set_contact():