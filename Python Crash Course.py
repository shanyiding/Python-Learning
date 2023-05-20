#!/usr/bin/env python
# coding: utf-8

# In[35]:


print("hello world")


# In[133]:


#LISTS[]: store multiple items in a single variable

animals=['cat','dog','rabbit','hamster','fish','monkey']
print(animals)
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[-1])

#[-1] is quick access to the last item of a list

print(animals[3]+" and "+animals[4])


# In[134]:


#Modifying an item in a list

animals[0]="panda"
print(animals)

#list.remove('item'): removing an item in a list

animals.remove('hamster')
print(animals)

#list.insert(position,item): insert an intem in a given position

animals.insert(3,'pigeon')
print(animals)


# In[135]:


#MORE ON LISTS
#list.append(): add an item to the end of a list, repeating ctrl+enter continues to add at the end

animals.append('gorilla')
print(animals)

#list.extend(iterable): add item that is separated letter by letter, will repeat if multiple ctrl+enter
#re-ctrl+enter to go back to non-repeated list length

animals.extend('ladybug')
print(animals)
animals.extend('2023')
print(animals)

#list.reverse(): reverse the items of a list

animals.reverse()
print(animals)

#list.copy(): return a copy of a list

animals.copy()
print(animals)


# In[137]:


#list.clear(): remove all items in a list

animals.clear()
print(animals)


# In[24]:


#DICTIONARIES{}: store value in key; {key1:value1, key 2:value2}

tree = {'color':'green','age':'10'}
print(tree['color'])
print(tree['age'])
age=tree['age']
color=tree['color']
print("You are "+str(color)+ " and " + str(age) +" years old")


# In[34]:


#EXAMPLE: the tree is green and 10 years old in 2001, yellow and 11 years old in 2002, red and 12 years old in 2003. What color and how old will it be in year x？

