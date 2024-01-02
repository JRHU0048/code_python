import jieba.posseg as pseg

text = "希望小胡天天开心，永远没烦恼，早日当院士"
words = pseg.cut(text)

for word, pos in words:
    print(word, pos)
    
#在上述代码中，pseg.cut函数将文本进行分词和词性标注，并返回一个生成器对象。通过迭代生成器对象，我们可以获取每个词语及其对应的词性。
