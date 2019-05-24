# 4号词云：同济大学介绍词云
# B站专栏：同济子豪兄 2019-5-23

# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
# 构建并配置词云对象w
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 调用jieba的lcut()方法对原始文本进行中文分词，得到string
txt = '同济大学（Tongji University），简称“同济”，是中华人民共和国教育部直属，由教育部、国家海洋局和上海市共建的全国重点大学，历史悠久、声誉卓著，是国家“双一流”、“211工程”、“985工程”重点建设高校，也是收生标准最严格的中国大学之一'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('output4-tongji.png')
