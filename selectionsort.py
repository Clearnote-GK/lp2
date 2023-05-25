#!/usr/bin/env python
# coding: utf-8

# In[8]:


def selectionSort(arr):
    n=len(arr)
    for i in range (n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
            
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
        print("Array after iteration",i+1, ":",arr)
        
    return arr
arr=[-9,20,3,-20,50,19]
print("Original array: ",arr)
sorted_arr =selectionSort(arr)
print("Sorted array:", sorted_arr)


# In[ ]:




