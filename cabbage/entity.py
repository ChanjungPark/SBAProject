from dataclasses import dataclass

# 전형적인 지도학습 entity
# context의 위치만 변경하면 됩니다
@dataclass
class Entity:

    context : str = 'C:/ChanjungPark/SBAProject/cabbage/data/' 
    fname : str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''