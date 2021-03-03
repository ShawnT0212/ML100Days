import numpy as np
#第一題 生成一個等差數列，首數為 0，尾數為 20，公差為 1 的數列。
data=np.arange(21)
# 第二題 列印出2 的倍數
for x in data:
    if x%2==0:
        print(x)
# 第三題 列印出 3的倍數
y=np.arange(3,21,3)
print(y)