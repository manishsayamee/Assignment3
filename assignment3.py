# -*- coding: utf-8 -*-
"""assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GNZrC1xG22l_tl1L8gcZnd0qKj3MmC8x
"""

# question 1.a
def BubbleSort(unsort):
  for i in range(len(unsort)-1,0,-1):
    for j in range(i):
      if unsort[j]>unsort[j+1]:
        temp=unsort[j]
        unsort[j]=unsort[j+1]
        unsort[j+1]=temp
  return unsort

unsort=[12,33,25,35,3]
BubbleSort(unsort)

a = [3,1,7,9,33,5,6]
def insertion(a):
  for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
      a[j+1]=a[j]
      j-=1
    a[j+1]=key
  return a

insertion(a)

# linear search
lst=[1,3,54,2,2,7,6,5,3]
def linearSearch(lst,a):
  for x in range(0,len(lst)):
    if lst[x]==a:
      return x
  
  return "Not fount"

linearSearch(lst,5)

# Binary Search
def BinarySearch(lst, lower, higher, a):
  if higher>0:
    mid= lower+(higher-lower)//2

    if lst[mid]==a:
      return mid
    elif lst[mid]<a:
      return BinarySearch(lst,mid+1, higher,a)
    else:
      return BinarySearch(lst,lower, mid-1,a)
  else:
    return "Not found"

a=[2,3,5,7,8,9,33,55]
BinarySearch(a, 0, len(a)-1, 33)

# interpolation 
def Interpolation(a, b):
  l=0
  h= len(a)-1
  while l<=h and b<=a[h] and b>=a[l]:
    if a[l]==a[h]:
      if a[l]==x:
        return l
      return -1
    pos = l + ((h-l)//(a[h]-a[l]))*(b-a[l])
    if a[pos]==b:
      return pos
    elif a[pos]<b:
      l= pos+1
    else:
      h=pos-1

a=[2,4,5,6,7,8,9,44]
Interpolation(a,8)

def TowerOfHanoi(n , A, B, C): 
    if n == 1: 
        return print("Move Disk 1 from rod",A,"to rod",B) 

    TowerOfHanoi(n-1, A, C, B) 
    print("Move disk",n,"from rod",A,"to rod",B) 
    TowerOfHanoi(n-1, C, B, A) 
          
# Driver code 
n = 2
TowerOfHanoi(n, 'A', 'C', 'B')  
# A, C, B are the name of rods

def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 
		L = arr[:mid] 
		R = arr[mid:] 

		mergeSort(L) 
		mergeSort(R) 

		i = j = k = 0

		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1

		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1
a=[1,3,8,9,3,1,0]
mergeSort(a)
print(a)

def partition(arr,low,high): 
	i = ( low-1 )		 
	pivot = arr[high]	

	for j in range(low , high): 

		if arr[j] < pivot: 

			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def quickSort(arr,low,high): 
	if low < high: 

		pi = partition(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

arr = [10, 80, 30, 90, 40, 50, 70] 
n=len(arr)
l=0
quickSort(arr,0,n-1)
print(arr)

