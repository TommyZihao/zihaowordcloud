# 1号词云：葛底斯堡演说黑色背景词云
# B站专栏：同济子豪兄 2019-5-23

# 导入词云制作第三方库wordcloud
import wordcloud

# 创建词云对象，赋值给w，现在w就表示了一个词云对象
w = wordcloud.WordCloud()

# 调用词云对象的generate方法，将文本传入
w.generate('and that government of the people, by the people, for the people, shall not perish from the earth.')

# 将生成的词云保存为output1.png图片文件，保存出到当前文件夹中
w.to_file('output1.png')
