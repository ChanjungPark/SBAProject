import sys
sys.path.insert(0, 'C:/ChanjungPark/SBAProject')
from titanic.entity import Entity
from titanic.service import Service

"""
### : 필요없거나 drop시키는 것

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

class Controller:
    def __init__(self):
        # print('TEST')
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        # print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)    
        print(f'>> Train 변수 : {this.train.columns}')
        print(f'>> Test 변수 : {this.train.columns}')
        return this

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) # payload
        this.test = service.new_model(test) # payload
        this.id = this.test['PassengerId'] # machine이에게는 이것이 문제(question)가 됩니다.
        # print(f'drop 전 변수 : {this.train.columns}')
        print(f'정제 전 Train 변수 : {this.train.columns}')
        print(f'정제 전 Test 변수 : {this.test.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        print(f'drop 후 변수 : {this.train.columns}')
        this = service.embarked_norminal(this)
        print(f'승선한 항구 정제결과: {this.train.head()}')
        this = service.title_norminal(this)
        print(f'타이틀 정제결과: {this.train.head()}')
        # name 변수에서 title 을 추출했으니 name 은 필요가 없어졌고, str 이니 
        # 후에 ML-lib 가 이를 인식하는 과정에서 에러를 발생시킬것이다.
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        print(f'나이 정제결과: {this.train.head()}')
        this = service.drop_feature(this, 'SibSp')
        this = service.sex_norminal(this)
        print(f'성별 정제결과: {this.train.head()}')
        this = service.fareBand_nominal(this)
        print(f'요금 정제결과: {this.train.head()}')
        this = service.drop_feature(this, 'Fare')
        print(f'#########  TRAIN 정제결과 ###############')
        print(f'{this.train.head()}')
        print(f'#########  TEST 정제결과 ###############')
        print(f'{this.test.head()}')
        print(f'######## train na 체크 ##########')
        print(f'{this.train.isnull().sum()}')
        print(f'######## test na 체크 ##########')
        print(f'{this.test.isnull().sum()}')
        return this

    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        print('&&&&&&&&&&&&&&&&& Learning 결과  &&&&&&&&&&&&&&&&')
        print(f'결정트리 검증결과: {service.accuracy_by_dtree(this)}')
        print(f'랜덤포리 검증결과: {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과: {service.accuracy_by_nb(this)}')
        print(f'KNN 검증결과: {service.accuracy_by_knn(this)}')
        print(f'SVM 검증결과: {service.accuracy_by_svm(this)}')

    def submit(self):   # machine이 됩니다. 이 단계에서는 케글에게 내 machine를 보내서 평가받게 하는 것입니다.
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv','test.csv')