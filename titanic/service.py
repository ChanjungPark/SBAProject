from titanic.entity import Entity
import sys
sys.path.insert(0, 'C:/ChanjungPark/SBAProject')
import pandas as pd
import numpy as np

"""
### : 필요없거나 편집시키거나 drop시키는 것
PassengerId, Survived는 답이니까 바뀌거나 편집되면 X
Ticket, Cabin은 쓰레기값

### PassengerId  고객ID,
### Survived 생존여부,  --> 머신러닝 모델이 맞춰야 할 답 
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
### Ticket 티켓번호,
Fare 요금,
### Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

class Service:
    def __init__(self):
        self.entity = Entity()  
        pass

    
    def new_model(self, payload) -> object:
        this = self.entity
        this.fname = payload
        return pd.read_csv(this.context + this.fname) # p.139  df = tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1) # train 은 답이 제거된 데이터셋이다. 

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] # label 은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1) # p.149 에 보면 훈련, 테스트 세트로 나눈다
        return this

    @staticmethod
    def pclass(this) -> objects:
        return this

    @staticmethod
    def name(this) -> objects:
        return this

    @staticmethod
    def sex(this) -> objects:
        return this

    @staticmethod
    def age(this) -> objects:
        return this

    @staticmethod
    def sibsp(this) -> objects:
        return this

    @staticmethod
    def parch(this) -> objects:
        return this

    @staticmethod
    def fare(this) -> objects:
        return this

    @staticmethod
    def embarked(this) -> objects:
        return this