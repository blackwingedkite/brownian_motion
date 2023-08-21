import numpy as np
import pandas as pd
covar = {}
stock_code = [1432,9943,2705,5478,6404,4735,
              8432,4104,6505,4581,1210,1216,1229,
              3533,5388,3596,2882,2890,"00888","00850"] 
for i in stock_code:
    try:
        data = pd.read_csv("stock/"+str(i)+".csv")
    except:
        data = pd.read_csv("stock/"+str(i)+" .csv")
    daily_returns = data["未調整收盤價(元)"].values
    covar[str(i)] = daily_returns[0:500]

df = pd.DataFrame(covar)
print(df)
returns = df.pct_change().dropna()
cov_matrix = returns.cov()
cov_threshold = 0.000001
selected_pairs = []
for i in range(len(cov_matrix.columns)):
    for j in range(i + 1, len(cov_matrix.columns)):
        cov_value = cov_matrix.iloc[i, j]
        # print(cov_value)
        if abs(cov_value) < cov_threshold:
            selected_pairs.append((cov_matrix.columns[i], cov_matrix.columns[j]))
print("可以投資的股票對：")
for stock1, stock2 in selected_pairs:
    print(f"{stock1} 和 {stock2}")