from flask import Flask
from flask import render_template, request
from price_prediction.cabbage  import Cabbage
from member.student import Student
from member.student import StudentService

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('join.html')

@app.route('/move/<path>')
def move(path):
    return render_template(f'{path}.html')

# method 는 총 4개가 있습니다.
# GET, POST, PUT, DELETE
# 그래서 이것들은 array 를 이룹니다.
# 그 array 이름은 methods 입니다.
# app 에서는 POST 하고 하면 인지하지 못하고 ['POST] 라고 해야 인지합니다.
# 그래서 아래 코드는 
# methds=['POST'] 로 바뀝니다. (method='POST' -> method=['POST'])
# 이런 methods 를 RESTful 이라고 합니다.
# https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html 참고
@app.route('/cabbage', methods=['POST'])
def cabbage():
    print('UI ~ API Connect Success !')
    avgTemp = request.form['avgTemp']
    minTemp = request.form['minTemp']
    maxTemp = request.form['maxTemp']
    rainFall = request.form['rainFall']
    print(f'avgTemp : {avgTemp}')
    print(f'minTemp : {minTemp}')
    print(f'maxTemp : {maxTemp}')
    print(f'rainFall : {rainFall}')
    cabbage = Cabbage()
    cabbage.avgTemp = avgTemp
    cabbage.minTemp = minTemp
    cabbage.maxTemp = maxTemp
    cabbage.rainFall = rainFall
    result = cabbage.service()
    print(f'**** PREDICTION : {result}')
    render_params = {}
    render_params['result'] = result
    return render_template('index.html', **render_params)

@app.route('/signup', methods=['POST'])
def signup():
    print(' ######  SIGNUP #########')
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    birth = request.form['birth']
    student = Student()
    student.id = id
    student.pwd = pwd
    student.name = name
    student.birth = birth
    service = StudentService()
    service.add_student(student)

if __name__ == "__main__":
    app.run()