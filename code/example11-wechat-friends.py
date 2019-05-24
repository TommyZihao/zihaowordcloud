# 11号词云：绘制你的微信好友个性签名词云
# B站专栏：同济子豪兄 2019-05-23

# 导入微信库ichat，中文分词库jieba
import itchat
import jieba

# 先登录微信，跳出登陆二维码
itchat.login()
tList = []
# 获取好友列表
friends = itchat.get_friends(update=True)

# 构建所有好友个性签名组成的大列表tList
for i in friends:
    # 获取个性签名
    signature = i["Signature"]
    if 'emoji' in signature:
        pass
    else:
        tList.append(signature)
text = " ".join(tList)

# 对个性签名进行中文分词
wordlist_jieba = jieba.lcut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio
mk = imageio.imread("chinamap.png")

# 导入词云制作库wordcloud
import wordcloud

# 构建并配置词云对象w，注意要加scale参数，提高清晰度
my_wordcloud = wordcloud.WordCloud(background_color='white',
                                   width=1000,
                                   height=700,
                                   font_path='msyh.ttc',
                                   max_words=2000,
                                   mask=mk,
                                   scale=20)
my_wordcloud.generate(wl_space_split)

nickname = friends[0]['NickName']
filename = "output11-{}的微信好友个性签名词云图.png".format(nickname)
my_wordcloud.to_file(filename)

# 显示词云图片
import matplotlib.pyplot as plt
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
print('程序结束')
