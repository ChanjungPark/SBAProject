variable(변하는 상태) vs constant(변하지 않는 상태)
그중에서 variable 은 분류가 가능합니다.
분류기준을 두고, 나누는데 크게 이분하면
cate, nominal(=: name)
다시 cate 는 ordinal(=: order), numeric(=: number)
그래서 결국은
ordinal, numeric, norminal 

==========================================================================

embarked 부터 하겠습니다.

머신러닝 교과서 p.138참고 - 누락된 값 처리 방식
지금 이 embarked 지우면 안되고 즉 dropna 를 쓰면 안되고 
p.139 대체하는 방식을 사용해야 합니다.

여기서 null 값 을 무엇으로 넣을 것인가 ?
평균값을 넣자고 책에는 명시되어 있습니다.
그러나 이 예제는 str 으로 평균을 구할 수 없습니다.
그래서 가장 많이 승선한 항구로 대체하겠습니다.
물론 통계를 왜곡할 수 있지만 그 null 의 수가 적으니 무시하기로 합니다.
왜냐하면 빈값이 있으면 아예 그 변수를 사용할 수 없어서 그것보다는 차선을 택하자는 생각입니다.
이 예제에서는 사우스햄튼에서 승선객의 비율이 높아서 S 로 대체하기로 합니다.
변수명은 ['변수명 '] , 변수값은 {'변수명':'변수값'}

    @staticmethod
    def sex_norminal(this) -> object:
        # male = 0, female = 1
        this.train['Sex'] = this.train['Sex'].map({'male':0, 'female':1})
        this.test['Sex'] = this.test['Sex'].map({'male':0, 'female':1})
        return this

코딩은 반복된 코드를 싫어합니다.
for(), while() 이 syntax 가 존재하는 이유.
그래서 위 코드에서 반복을 피하기 위해 (지도학습의 숙명인 train과 test 둘다 편집해야하는 상황)
다음과 같은 코드가 나옵니다.

    @staticmethod
    def sex_norminal(this) -> object:
        # male = 0, female = 1
        combine = [this.train, this.test] # train과 test 가 묶입니다. 
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train # overriding
        this.test = this.test
        return this