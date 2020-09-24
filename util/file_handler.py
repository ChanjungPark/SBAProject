from dataclasses import dataclass

'''
context : C:/ChanjungPark/SBAProject
fname : /titanic/data/
'''

# 전형적인 지도학습 entity
# context의 위치만 변경하면 됩니다
@dataclass
class FileReader:

    context : str = '' 
    fname : str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''