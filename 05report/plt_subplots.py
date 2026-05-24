import matplotlib.pyplot as plt
# 导入NumPy库
import numpy as np

# 第1个子图
x1 = np.array([0, 1, 2, 3, 4, 5, 6])
y1 = np.random.randint(low=1, high=100, size=7).tolist()  # 产生随机数
plt.subplot(1, 2, 1)
plt.bar(x1, y1)  # 绘制柱形图
plt.title("Graph 1")
# 第2个子图
x2 = np.array([1, 2, 3, 4])
y2 = np.array([1, 4, 9, 16])
plt.subplot(1, 2, 2)
plt.scatter(x2, y2)  # 绘制散点图
plt.title("Graph 2")
plt.suptitle("Test subplot")     # 总标题
plt.show()
