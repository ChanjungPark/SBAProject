from dataclasses import dataclass

@dataclass
class Entity:
    
    context: str = 'C:/ChanjungPark/SBAProject/titanic/data/'
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''
