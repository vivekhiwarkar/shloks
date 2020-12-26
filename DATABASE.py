#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import pytesseract
import matplotlib.pyplot as plt
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'auto')


# In[1]:


import pyrebase


# In[2]:
def textRec(imgName):


    pytesseract.pytesseract.tesseract_cmd=r'D:\Softwares\Tesseract-OCR\tesseract.exe'


    # In[3]:


    img=cv2.imread(r'D:\project\\'+imgName) 


    # In[ ]:





    # In[4]:


    cv2.imshow('Basic',img)


    # In[5]:


    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("IMAE",gray)


    # In[6]:


    ret, threshold=cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
    cv2.imshow("THRESHOLD",threshold)


    # In[7]:


    gaus=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
    cv2.imshow("GAUS",gaus)


    # In[9]:


    text=pytesseract.image_to_string(gaus)
    print('Here ?')
    print(text,sep='\n')
    print('YES ?')
    return text


    # In[23]:

'''
    name=text.index('Name')
    name
    sp=text.index(' ')
    sp


    # In[28]:


    text[name-1]


    # In[20]:


    names=[]
    maths=[]
    physics=[]
    chem=[]
    bio=[]
    cs=[]


    # In[21]:


    print("Enter the number of students")
    n=int(input())


    # In[48]:


    names=i+47
    text[names]


    # In[55]:


    for e in text[names:names+25]:
        if(e==' '):
            end=text.index(e)
            print(end)
            


    # In[53]:


    text[names:names+25]


    # In[44]:


    name1=text[4:16]
    name1
    name2=text[(i+19):(i+29)]


    # In[17]:


    names.append(name2)
    serial.append('2')


    # In[18]:


    names


    # In[19]:


    import pandas as pd


    # In[20]:


    data=pd.DataFrame()


    # In[21]:


    data['Serial Number']=serial
    data['Name']=names


    # In[22]:


    data


    # In[32]:


    data.to_csv('C:/Users/Shlok/Desktop/database.csv',index=False)


    # In[ ]:
'''


'''
if __name__ == "__main__":
    main()'''