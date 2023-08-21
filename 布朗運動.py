import numpy as np
import pandas as pd

def monte_carlo_simulator(num,num_days=252):
    # 讀取csv檔案
    try:
        data = pd.read_csv("stock/"+num+".csv")
    except:
        data = pd.read_csv("stock/"+num+" .csv")
    daily_returns = data["日報酬率 %"].values
    initial_price = data["未調整收盤價(元)"].iloc[0]
    # 計算每日報酬率的平均值和標準差
    mean_return = np.mean(daily_returns)
    std_dev = np.std(daily_returns)
    
    # 建立一個空的list來存儲模擬的價格路徑
    price_paths = []
    
    # 進行蒙地卡羅模擬
    for _ in range(1000):
        prices = [initial_price]
        for _ in range(num_days):
            # 使用幾何布朗運動模型來計算下一日的股票價格
            next_price = prices[-1] * np.exp((mean_return - 0.5 * std_dev**2) * (1/num_days) + std_dev * np.sqrt(1/num_days) * np.random.standard_normal())
            prices.append(next_price)
        price_paths.append(prices)
    
    return price_paths,initial_price

stock_code = [1432,9943,2705,5478,6404,4735,
              8432,4104,6505,4581,1210,1216,1229,
              3533,5388,3596,2882,2890,"00930","00888","00850"] 
re = []
sentence = []
for i in stock_code:
    final = []
    paths, price = monte_carlo_simulator(str(i))
    for j in range(len(paths)):
        final.append(paths[j][-1])
    sentence.append(str(i) + "預估未來股價： "+str(np.average(final)))
    sentence.append(str(i) + "漲跌： "+str(100*((np.average(final))-price)/price)+"%")
    print(str(i) + "預估未來股價： "+str(np.average(final)))
    print(str(i) + "漲跌： "+str(100*((np.average(final))-price)/price)+"%")
    re.append(100*((np.average(final))-price)/price)
print("==========")
print(np.average(re))

#印出前5個模擬路徑的結果
for i in range(5):
    print(f"模擬路徑 {i+1}: {paths[i]}")

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
for i in range(500):
    plt.plot(range(len(paths[i])), paths[i], label=f"Path {i+1}")

plt.xlabel("Day")
plt.ylabel("Stock Price")
plt.title(f"Monte Carlo Simulation for {stock_code} Stock")
plt.legend()
plt.grid(True)
plt.show()
