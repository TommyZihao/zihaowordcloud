import jieba
print('\n')
text = '动力学和电磁学'
print('这是一段文本：',text)
print('\n')
print('{:-^50}'.format('下面的红色提示是导入语言模型时的正常提示，不用管它'))
textlist = jieba.lcut(text)
print('{:-^50}'.format('精确模式：每个字只用一遍，不存在冗余词汇'))
print('\n')
print('分词之后生成的列表为',textlist)
print('\n')

print('{:-^50}'.format('全模式：把每个字可能形成的词汇都提取出来，存在冗余'))
textlist = jieba.lcut(text,cut_all=True)
print('\n')
print('分词之后生成的列表为',textlist)
print('\n')

print('{:-^50}'.format('搜索引擎模式：将全模式分词的结果从短到长排列好'))
textlist = jieba.lcut_for_search(text)
print('\n')
print('分词之后生成的列表为',textlist)

