#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，
# 拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、
# 第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
if __name__ == '__main__':
    i = 0                                 #I是猴子
    j = 1                                 #因为求最少，所以假设最后一份只有一个
    x = 0                                 #X:第几只猴子分之前的桃子数
    while (i < 5) :
        x = 4 * j
        for i in range(0,5) :
            if(x%4 != 0) :
                break
            else :
                i += 1
            x = (x/4) * 5 +1
        j += 1
    print x