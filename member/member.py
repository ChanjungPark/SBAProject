import sqlite3

class Student:
    id: str = ''
    pwd: str = ''
    name: str = ''
    birth: str = ''
    regdate: str = ''

    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cursor = conn.cursor()

class StudentDao:
    
    def create(self):
        # cursor(커서) : 데이터베이스 작업을 수행하고 있는 메모리 공간
        try:
            # excute : sql 구문을 실행해주는 함수
            self.cursor.execute("drop table students")
        except sqlite3.OperationalError as err:
            print("테이블이 존재하지 않습니다.")

        self.cursor.execute(
            '''create table students
            (id text primary key, pwd text, name text, birth text)'''
        )
        self.cursor.commit()

    def insert_one(self, payload):
        # payload = ('lee', '이승기', '1989/11/11')
        sql = "insert into students(id, pwd, name, birth) values ('{student.id}', '{student.pwd}', '{student.name}', '{student.birth}')"
        self.cursor.execute(sql)
        self.cursor.commit()

    def insert_many(self):
        data = [('jo', '조용필', '1985/12/31'), ('ko', '고아라', '1970/07/17'), ('sim', '심형래', '1950/06/06')]
        # ?: place holder : 치환되어야 할 어떤 대상
        # 데이터 유형에 상관없이 외따옴표 적지 X
        query = """
            INSERT INTO member(userid, password, phone) VALUES ('?, ?, ?')
        """
        self.cursor.executemany(query, data)
        self.cursor.commit()

    def fetch_one(self):
        cursor = self.cursor
        findID = 'ko'
        sql = "select * from students where id = '%s'" % (findID)
        cursor.execute(sql)
        result = cursor.fetchone() # fetch 해줘야 함
        print(type(result)) # 튜플 형태로 리턴
        if result != None:
            print('아이디 : ' + result[0], end='')
            print(', 이름 : ' + result[1], end='')
            print(', 생일 : ' + result[2], end='')
        else:
            print('문제가 있습니다.')
        return result

    def fetch_list(self):
        cursor = self.cursor
        sql = 'select * from students order by name desc'
        for id, name, birth in cursor.execute(sql): # 다중 데이터는 for문으로 바로 출력가능
            print(id + '#' + name + '#' + birth)
        print('-'*20)

    def fetch_by_name(self, name):
        cursor = self.cursor
        sql = f"select * from students where name like '%{name}%"
        cursor.execute(sql)
        return cursor.fetchall()

    def fetch_count(self):
        cursor = self.cursor
        sql = f'select * from students'
        return cursor.execute(sql)

    def fetch_all(self):
        cursor = self.cursor
        cursor.execute('select * from students')
        return cursor.fetchall()
        
    def login(self):
        cursor = self.cursor

    def update(self, id, name):
        # 'id'가 'lee'인 친구의 이름을 '이문세'로 바꾸세요.
        cursor = self.cursor
        sql = f"update students set name = '{name}' where id = '{id}'"
        cursor.execute(sql)
        print(cursor.rowcount) # 성공 여부
        cursor.commit()

    def delete(self, id):
        # 'id' 데이터를 삭제하세요.
        cursor = self.cursor
        sql = f"delete from students where id = '%{id}'"
        cursor.execute(sql)
        print(cursor.rowcount)
        self.conn.commit()

        # cursor.close()
        # conn.close()  # web 상에서는 close 하지 않음

class StudentService:
    pass