'''
    Description: Python期末结课作业
    Create by JetBrains PyCharm
    Author:马骏超
    Time:2018/12/15 11:00
'''
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('buddymove_holidayiq.csv', sep=',', header=None, encoding='utf-8')
#print(data)

#print(data.shape)#数据集格式(250,7)

##1.1 六个场景的总评论数柱状图

sports = religious = nature = theatre = shopping = picnic = 0

for i in range(1, 249):
    sports = sports + int(data[1][i])
    religious = religious + int(data[2][i])
    nature = nature + int(data[3][i])
    theatre = theatre + int(data[4][i])
    shopping = shopping + int(data[5][i])
    picnic = picnic + int(data[6][i])

#print(sports);print(religious);print(nature);print(theatre);print(shopping);print(picnic);

labels = ['体育场馆', '宗教机构', '自然景观', '剧院展览', '商场购物', '公园野餐']
newdata = [sports, religious, nature, theatre, shopping, picnic]
plt.title('六个场景的总评论数柱状图')
#plt.savefig('pic/六个场景的总评论数柱状图.png')
plt.bar(range(len(newdata)), newdata, tick_label=labels)
plt.show()

##1.2 六个场景的总评论数扇形图

labels = labels = ['体育场馆', '宗教机构', '自然景观', '剧院展览', '商场购物', '公园野餐']
sizes = [2.1, 18.4, 20.9, 19.5, 18.9, 20.2]
colors = ['red', 'yellow', 'blue', 'green', 'gray', 'orange']
explode = (0.05, 0, 0, 0, 0, 0)
patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance=1.1, autopct='%2.0f%%', shadow=True, startangle=90, pctdistance=0.6)
for t in l_text:
        t.set_size = 30
for t in p_text:
        t.set_size = 20
plt.axis('equal')
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.grid()
#plt.savefig('pic/六个场景的总评论数饼状图.png')
plt.show()

##2.1 六个评论方向的最多人数柱状图

sports = religious = nature = theatre = shopping = picnic = 0
most = [0, 0, 0, 0, 0, 0]
for i in range(1, 250):
    for j in range(1, 7):
        most[j-1] = int(data[j][i])

    most.sort(reverse=True)
    #print(most)

    if most[0] == int(data[1][i]):
        sports = sports+1
    if most[0] == int(data[2][i]):
        religious = religious+1
    if most[0] == int(data[3][i]):
        nature = nature+1
    if most[0] == int(data[4][i]):
        theatre = theatre+1
    if most[0] == int(data[5][i]):
        shopping = shopping+1
    if most[0] == int(data[6][i]):
        picnic = picnic+1

#print(sports);print(religious);print(nature);print(theatre);print(shopping);print(picnic);

labels = ['体育场馆', '宗教机构', '自然景观', '剧院展览', '商场购物', '公园野餐']
newdata = [sports, religious, nature, theatre, shopping, picnic]
plt.title('六个评论方向的最多人数柱状图')
#plt.savefig('pic/六个评论方向的最多人数柱状图.png')
plt.bar(range(len(newdata)), newdata, tick_label=labels)
plt.show()

#2.2 六个评论方向的最多人数扇形图

labels = labels = ['体育场馆', '宗教机构', '自然景观', '剧院展览', '商场购物', '公园野餐']
sizes = [0.0, 7.4, 39.0, 20.2, 19.9, 13.5]
colors = ['red', 'yellow', 'blue', 'green', 'gray', 'orange']
explode = (0.05, 0, 0, 0, 0, 0)
patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance=1.1, autopct='%2.0f%%', shadow=True, startangle=90, pctdistance=0.6)
for t in l_text:
        t.set_size = 30
for t in p_text:
        t.set_size = 20
plt.axis('equal')
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.grid()
#plt.savefig('pic/六个评论方向的最多人数扇形图.png')
plt.show()

#3.1 6个评论方向的留言人数趋势

#3.1.1 体育场馆的留言人数趋势

a = []
for i in range(0, 250):
    a.append(0)

for i in range(1, 250):
    a[i] = data[1][i]

#print(a)

m = 0
n = 0
b = []

for j in range(0, 250):
    m = m + int(a[j])
    n = n + 1
    if j == 249:
        b.append(m / 9)
        m = 0
        n = 0
        break
    if n == 10:
        b.append(m / 10)
        m = 0
        n = 0

#print(b)

pl = plt.figure()
ax = pl.add_subplot(1, 1, 1)
plt.plot(np.arange(1, 26), b[:], linestyle='--', marker='o')
plt.xlabel('次')
plt.ylabel('平均评论数')
plt.xticks(range(1, 27, 1), range(1, 27, 1), rotation=40)
plt.ylim(0, 25)
plt.title('体育场馆的留言人数趋势')
#plt.savefig('pic/体育场馆的留言人数趋势.png')
plt.show()

#3.1.2 宗教机构的留言人数趋势

a = []
for i in range(0, 250):
    a.append(0)

for i in range(1, 250):
    a[i] = data[2][i]

m = 0
n = 0
b = []

for j in range(0, 250):
    m = m + int(a[j])
    n = n + 1
    if j == 249:
        b.append(m / 9)
        m = 0
        n = 0
        break
    if n == 10:
        b.append(m / 10)
        m = 0
        n = 0

#print(b)

pl = plt.figure()
ax = pl.add_subplot(1, 1, 1)
plt.plot(np.arange(1, 26), b[:], linestyle='--', marker='o')
plt.xlabel('次')
plt.ylabel('平均评论数')
plt.xticks(range(1, 27, 1), range(1, 27, 1), rotation=40)
plt.ylim(0, 160)
plt.title('宗教机构的留言人数趋势')
#plt.savefig('pic/宗教机构的留言人数趋势.png')
plt.show()

#3.1.3 自然景观的留言人数趋势

a = []
for i in range(0, 250):
    a.append(0)

for i in range(1, 250):
    a[i] = data[3][i]

m = 0
n = 0
b = []

for j in range(0, 250):
    m = m + int(a[j])
    n = n + 1
    if j == 249:
        b.append(m / 9)
        m = 0
        n = 0
        break
    if n == 10:
        b.append(m / 10)
        m = 0
        n = 0

#print(b)

pl = plt.figure()
ax = pl.add_subplot(1, 1, 1)
plt.plot(np.arange(1, 26), b[:], linestyle='--', marker='o')
plt.xlabel('次')
plt.ylabel('平均评论数')
plt.xticks(range(1, 27, 1), range(1, 27, 1), rotation=40)
plt.ylim(0, 210)
plt.title('自然景观的留言人数趋势')
#plt.savefig('pic/自然景观的留言人数趋势.png')
plt.show()

#3.1.4 剧院展览的留言人数趋势

a = []
for i in range(0, 250):
    a.append(0)

for i in range(1, 250):
    a[i] = data[4][i]

m = 0
n = 0
b = []

for j in range(0, 250):
    m = m + int(a[j])
    n = n + 1
    if j == 249:
        b.append(m / 9)
        m = 0
        n = 0
        break
    if n == 10:
        b.append(m / 10)
        m = 0
        n = 0

#print(b)

pl = plt.figure()
ax = pl.add_subplot(1, 1, 1)
plt.plot(np.arange(1, 26), b[:], linestyle='--', marker='o')
plt.xlabel('次')
plt.ylabel('平均评论数')
plt.xticks(range(1, 27, 1), range(1, 27, 1), rotation=40)
plt.ylim(0, 160)
plt.title('剧院展览的留言人数趋势')
#plt.savefig('pic/剧院展览的留言人数趋势.png')
plt.show()

#3.1.5 商场购物的留言人数趋势

a = []
for i in range(0, 250):
    a.append(0)

for i in range(1, 250):
    a[i] = data[5][i]

m = 0
n = 0
b = []

for j in range(0, 250):
    m = m + int(a[j])
    n = n + 1
    if j == 249:
        b.append(m / 9)
        m = 0
        n = 0
        break
    if n == 10:
        b.append(m / 10)
        m = 0
        n = 0

#print(b)

pl = plt.figure()
ax = pl.add_subplot(1, 1, 1)
plt.plot(np.arange(1, 26), b[:], linestyle='--', marker='o')
plt.xlabel('次')
plt.ylabel('平均评论数')
plt.xticks(range(1, 27, 1), range(1, 27, 1), rotation=40)
plt.ylim(0, 160)
plt.title('商场购物的留言人数趋势')
#plt.savefig('pic/商场购物的留言人数趋势.png')
plt.show()

#3.1.6 公园野餐的留言人数趋势

a = []
for i in range(0, 250):
    a.append(0)

for i in range(1, 250):
    a[i] = data[6][i]

m = 0
n = 0
b = []

for j in range(0, 250):
    m = m + int(a[j])
    n = n + 1
    if j == 249:
        b.append(m / 9)
        m = 0
        n = 0
        break
    if n == 10:
        b.append(m / 10)
        m = 0
        n = 0

#print(b)

pl = plt.figure()
ax = pl.add_subplot(1, 1, 1)
plt.plot(np.arange(1, 26), b[:], linestyle='--', marker='o')
plt.xlabel('次')
plt.ylabel('平均评论数')
plt.xticks(range(1, 27, 1), range(1, 27, 1), rotation=40)
plt.ylim(0, 200)
plt.title('公园野餐的留言人数趋势')
#plt.savefig('pic/公园野餐的留言人数趋势.png')
plt.show()
