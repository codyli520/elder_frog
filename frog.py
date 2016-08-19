#! /usr/bin/env python
#coding:UTF-8           

import random

i=0

print'*******猜数字，为长者续命********\n\t口..口'
while 1:
    xnum = random.randint(0,9)
    print'*********************************'
    num = raw_input('请您输入0到9任一个数(输入\'exciting\'退出): ') 
    
    if 'exciting' in num.lower():
        print'我以一个长者的身份和你们说啊，闷声大发财，\n美国的华莱士比你们不知道高到哪里去了，我和他谈笑风生'
        break
    if not num.isdigit():
        print('I\'m angry ! 您输入的不是数字!') 
    elif int(num) < 0 or int(num) >= 10:
        print('I\'m angry ! 您输入的数字不在范围内!')
    
    else:
        num = int(num)
        if num == xnum:
            print('Excited，长者＋1s！')
        elif num > xnum:
            print('''猜大了!\n哈哈,正确答案是:%s!\n你们啊还是Too young！\n''' %(xnum))
        elif num < xnum:
            print('''猜小了!\n哈哈,正确答案是:%s!\n你们啊还是Too young！\n''' %(xnum))

