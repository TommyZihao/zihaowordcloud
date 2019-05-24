# 2号词云：面朝大海，春暖花开
# B站专栏：同济子豪兄 2019-5-23

import wordcloud

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,height=700,background_color='white',font_path='msyh.ttc')

# 调用词云对象的generate方法，将文本传入
w.generate('从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')

# 将生成的词云保存为output2-poem.png图片文件，保存到当前文件夹中
w.to_file('output2-poem.png')
