import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取停用词文件
stopwords = set()
with open(r"C:\Users\Jr.hu\Desktop\stopword.txt", 'r', encoding='utf-8') as file:
    for line in file:
        stopwords.add(line.strip())

# 读取txt文件
with open(r"C:\Users\Jr.hu\Desktop\奈雪的茶用户评论.txt", 'r', encoding='utf-8') as file:
    text = file.read()

# 将文本进行处理，将多行文本拼接成单行
text = text.replace('\n', '')

# 使用jieba进行分词同时排除停用词
words = jieba.cut(text)
words = [word for word in words if word not in stopwords]

# 统计词频
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# 生成词云
wordcloud = WordCloud(font_path =r'C:\Users\Jr.hu\PycharmProjects\pythonProject1\像素图\AliPuHui-Bold.ttf',width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# 显示词云图
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存词频到文件
with open('word_freq.txt', 'w', encoding='utf-8') as file:
    for word, freq in word_freq.items():
        file.write(f"{word}\n")
#
#         # 将词频保存到xlsx文件
#         output_workbook = openpyxl.Workbook()
#         output_sheet = output_workbook.active
#         output_sheet.append(['词语', '出现次数'])
#         for word, count in word_counts.items():
#             output_sheet.append([word, count])
#         output_workbook.save('word_counts.xlsx')
