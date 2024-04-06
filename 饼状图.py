import matplotlib.pyplot as plt

# 饼状图的标签
labels = '包装饮用水', '果汁饮料', '其他', '即饮茶','碳酸饮料'
# 每个标签对应的数值
sizes = [37.64, 14.33, 13.13, 19.64,15.26]
# 指定的颜色
colors = ['#D5EA66', '#80BF66', '#55AA66', '#2A9466','#007F66']

# 绘制饼状图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.show()
