
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签


# 配置各种分布的参数
distributions_data = {
'均匀分布': np.random.uniform(low=-2, high=2, size=1000),
'正态分布': np.random.normal(loc=0, scale=1, size=1000),
'指数分布': np.random.exponential(scale=1, size=1000),
't分布': np.random.standard_t(df=10, size=1000),
'伽马分布': np.random.gamma(shape=2, scale=1, size=1000),
'贝塔分布': np.random.beta(a=2, b=5, size=1000),
'卡方分布': np.random.chisquare(df=2, size=1000)
}

data = distributions_data['卡方分布']

distributions_with_names = [
    (stats.uniform, '均匀分布'),
    (stats.norm, '正态分布'),
    (stats.expon, '指数分布'),
    (stats.t, 't 分布'),
    (stats.gamma, '伽马分布'),
    (stats.beta, '贝塔分布'),
    (stats.chi2, '卡方分布')
]

# 进行拟合和检验
extended_results_with_names_and_params = []
for distribution, name in distributions_with_names:
# 拟合分布到数据
params = distribution.fit(data)
# 计算拟合优度
    D, p = stats.kstest(data, distribution.name, args=params)
# 保存结果和分布参数
    extended_results_with_names_and_params.append((name, D, p, params))

# 找到p值最大的分布及其参数
best_fit_name, best_fit_D, best_fit_p, best_fit_params = max(extended_results_with_names_and_params, key=lambda item: item[2]) 

# 生成描述性的文本
if best_fit_p > 0.05:
    description_cn = f"根据Kolmogorov-Smirnov检验的结果，这组数据最符合{best_fit_name}，因为其检验的p值为{best_fit_p:.3f}，远高于0.05，" \
f"表明数据与该分布的吻合度很高，没有统计显著性差异。分布参数为：{best_fit_params}"
else:
    description_cn = "根据Kolmogorov-Smirnov检验的结果，没有一个分布的p值高于0.05，这意味着没有一个分布能够很好地拟合这组数据。"

sns.set(style='white',context='talk',font='SimHei')
sns.set_context("notebook",rc={"ytick.labelsize": 0})

plt.figure(figsize=(10, 6))
ax = sns.histplot(data, bins=30, kde=True, color='blue')
ax.set_title(f"符合{best_fit_name}", fontsize=15)
ax.set_xlabel('数值', fontsize=12)
ax.set_ylabel('频率', fontsize=12)
plt.show()

