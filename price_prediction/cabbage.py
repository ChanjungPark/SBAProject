import sys
sys.path.insert(0, 'C:/ChanjungPark/SBAProject')
from util.file_handler import FileReader
import numpy as np
import pandas as pd

class Model:
    def __init__(self):
        self.fileReader = FileReader()
    
    def new_model(self, payload) -> object:
        this = self.fileReader
        this.context = 'C:/ChanjungPark/SBAProject/kaggle/data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

if __name__ == '__main__':
    m = Model()
    dfname = m.new_model('price_data.csv')
    print(dfname.head())