import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# check prophet version
import fbprophet
from fbprophet import Prophet
# print version number
print('Prophet %s' % fbprophet.__version__)

# load the dataset
path = '../input/corn2015-2017/corn2013-2017.txt'
df = pd.read_csv(path, sep=',',header=None, names=['date','price'])
df['date'] = pd.to_datetime(df['date'])
# show first few rows
df.head()