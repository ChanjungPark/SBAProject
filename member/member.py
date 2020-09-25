import sqlite3

class Member:
    userid: str = ''
    password: str = ''
    phone: str = ''
    regdate: str = ''

    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')

    def create(self):
        query = '''
            CREATE TABLE IF NOT EXISTS member(
                userid VARCHAR(10) PRIMARY KEY,
                password VARCHAR(10),
                phone VARCHAR(10),
                regdate DATE DEFAULT CURRENT_TIMESTAMP
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_many(self):
        data = [
            ('lee', '1', '010-1111-1111'),
            ('kim', '1', '010-2222-2222'),
            ('lee', '1', '010-3333-3333')
        ]
        query = '''
            INSERT INTO member(userid, password, phone) VALUES (?, ?, ?)
        '''
        self.conn.executemany()

    def fetch_one(self):
        pass

    def fetch_all(self):
        pass

    def login(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass