import pandas as pd

# 读取Excel文件
df = pd.read_excel('wenjuanyi.xlsx')

# 选择学号和填写时间的列
data = df[['学号', '填写时间']]

# 将填写时间列转换为字符串
data['填写时间'] = data['填写时间'].astype(str)

# 使用groupby()和agg()函数对学号进行分组，统计每个学号的出现次数和填写时间的合并
grouped_data = data.groupby('学号').agg({'学号': 'count', '填写时间': lambda x: ', '.join(x)})

# 重命名列名
grouped_data.columns = ['出现次数', '提交时间']

# 重置索引
grouped_data.reset_index(inplace=True)

# 将结果保存到新的Excel文件中
grouped_data.to_excel('result_with_one.xlsx', index=False)
