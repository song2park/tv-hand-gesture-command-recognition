# get database

import numpy as np
import pandas as pd

class Database:
    def __init__(self, mode: str ='train'):
        self.mode = mode
        self.path = self.setFilePath()
        self.data = self.loadData()

    def __sizeof__(self):
        return len(self.data)

    def __len__(self):
        return len(self.data)

    def setFilePath(self):
        return 'D:\\Dataset\\TV-hand-gesture-recognition\\train.csv' if self.mode == 'train' else 'D:\\Dataset\\TV-hand-gesture-recognition\\test.csv'

    def loadData(self):
        return pd.read_csv(self.path, header=0)

    def getVideoFile(self, idx: int):
        if self.data is None:
            return None

        return self.data.iloc[idx]