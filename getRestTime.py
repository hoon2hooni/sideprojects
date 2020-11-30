#!/usr/bin/env python
# coding: utf-8

# In[101]:


import os


# In[102]:


def getRestTime(path,n): #text경로, 문장 간격
    arr =[]
    hours = 0
    minutes = 0
    seconds = 0
    with open(path,'r',encoding ='utf-8') as r:
        lineArr =r.readlines()
    for i in range(0, len(lineArr), n):
        arr.append(lineArr[i][-7:-2]) # 10:22)\n
                                    # -7    -2
    for time_s in arr:
        if time_s != '': 
            minutes += int(time_s[:2])
            seconds += int(time_s[3:])
    
    minutes += seconds //60
    hours = minutes//60
    minutes -= 4*60
    print(f'남은 강의시간 {hours}시간 {minutes}분')


# In[103]:


getRestTime('C:/Users/hoon2/Desktop/sideProject/howmuch.txt',3)


# In[ ]:




