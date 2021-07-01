#!/usr/bin/env python
# coding: utf-8

# # assignment 1

# ### 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed  in a comma-separated sequence on a single line

# In[12]:


li=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        li.append(i)
print(li)        
        
        


# ### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. 

# In[24]:


firstname=input("enter your first name ")
lastname=input("enter yout last name ")
print(lastname+"  "+firstname)
    


# ## 3. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3 

# In[28]:


d=12  #diameter
r=d/2 #radius is the half of diameter
vol=(4/3)*3.14*r*r*r #value of pie is 3.14
print("the volume of sphere is : ",vol)


# In[ ]:




