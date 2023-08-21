import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
sns.set()
import tejapi
tejapi.ApiConfig.api_key = 'LVKpS4S9gTN2YRJcQsXPWdx3InBFIQ'
tejapi.ApiConfig.ignoretz = True
ticker = [] #多幾個
ret = tejapi.get('TWN/EWPRCD2', # 我這邊需要日報酬率
                  coid = ticker,
                  mdate = {'gte':'20200101'},
                  opts = {'columns': ['coid', 'mdate', 'roia']},
                  chinese_column_name = True,
                  paginate = True)
ret = ret.set_index('年月日')
RetData = {}
for i in ticker:
    r = ret[ret['證券代碼'] == i]
    r = r['日報酬率 %']
    RetData.setdefault(i, r)
RetData = pd.concat(RetData, axis = 1)
RetData = RetData * 0.01
#平均報酬
Mean = pd.DataFrame(list(np.mean(RetData[i]) for i in RetData.columns), index=RetData.columns, columns = ['平均報酬'])
#共變異數
covMatrix = RetData.cov()
print(covMatrix)