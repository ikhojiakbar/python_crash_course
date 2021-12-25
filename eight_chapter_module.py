#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_pizza(size, *args):
    print('\nMaking ' + str(size) + '-inch pizza with the following toppings: ')
    for topping in args:
        print('- ' + topping)


# In[ ]:




