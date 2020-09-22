class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name # self.name 과  name 은 서로 다른 존재인데, 할당함으로써 연결됨
        self.phone = phone
        self.email = email
        self.addr = addr  

    def print_info(self):
        print(f'이름 : {self.name}, 전화번호: {self.phone}, 이메일: {self.email}, 주소: {self.addr}') 
        # self.name 과  name 은 서로 다른 존재이므로 {self.name} 과 {name} 은 서로 다른 상태이다.

    @staticmethod
    def set_contact():
        name = input('이름')  # self.name 과  name 은 서로 다른 존재
        phone = input('전화번호')
        email = input('이메일')
        addr = input('주소')
        contact = Contact(name, phone, email, addr) 
        # Contact 는 클래스명, contact 는 인스턴스명 이 된다. 대소문자로 구분해 주는 것 권장
        return contact

    @staticmethod
    def get_contact(clist):
        for i in clist:
            i.print_info() # 8번라인에 선언된 메소드(클래스 내부에 선언된 함수), 함수는 클래스 밖에 있어요....

    @staticmethod
    def del_contact(clist, name):
        for i, t in enumerate(clist):  # i 는 인덱스, t 는 요소(인스턴스)를 출력한다.
            if t.name == name:
                del clist[i]

    @staticmethod
    def print_menu():
        print('1 연락처 입력')
        print('2 연락처 출력')
        print('3 연락처 삭제')
        print('4 종료')
        menu = input('메뉴선택: ')
        return menu

    @staticmethod
    def run():
        clist = []
        while 1:
            menu = Contact.print_menu()
            if menu == '1':
                t = Contact.set_contact()
                clist.append(t)

            if menu == '2':
                Contact.get_contact(clist) # static method 는 클래스가 직접 접근함.

            if menu == '3':
                name = input('삭제할 이름')
                Contact.del_contact(clist, name)

            elif menu == '4':
                break
if __name__ == '__main__':
    Contact.run()