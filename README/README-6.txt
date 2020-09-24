context : object(class = static, instance = dynamic) 가 존재하는 영역

https://flearning-blog.tistory.com/230 참고
Agile <-> Waterfall

MVC 패턴 구조에서 개발을 합니다
Model *.py + TF (SKlearn, keras)
View reactjs
Controller app.py Flask
Database : mariadb
Server : AWS

1. 개발환경 설정 -> context complete !!
1.1 Model 개발환경 완료
1.2 View 개발환경 완료
1.3 Controller 개발환경 : 

content 를 투입... context
==========================================================================
이제 modeling 환경세팅 끝
view 환경세팅 끝

둘을 연결할 networking setiing
==========================================================================
**********************************************************
********* cabbage 하면서 이제 STEP 2 로 넘어갑니다 *********
**********************************************************
STEP 2의 목표
1. Model: Python OOP 에서 reuse 를 고민합니다.
2. View: React 에서 입력한 데이터를 주고, Flask가 보낸 대답을 출력합니다.
3. Conroller: Flask 에서 React 가 보낸 데이터를 받아서 Python 모델이 주고, 그 예상값을 다시 React 에게 전달합니다.
기존 entity, service, controller 를 매번 만드는 것은 중복된 코드가 많이 생성되고
파일의 숫자를 3배수로 늘려서 복잡한 구조가 됩니다. 
따라서 util 폴더를 만들어서 공유하는 기능을 빼고(extract)
controller, service, entity 파트를 한 파일로 몰아서 한 컨텐츠당 하나의 파이썬 파일을 
사용하는 구조로 바꿉니다.