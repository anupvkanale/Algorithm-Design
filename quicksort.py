import random

def quicksort(inp, compcount):
  '''
  Function to sort an integer array in ascending order, using the
  quicksort algorithm as discussed in the Algorithms class on Coursera
  '''
  
  if (len(inp)>1):
    compcount+=len(inp)-1
    choosePivot(inp)
    pivot = inp[0]
    i=1;

    # Partitioning the array by swapping whenever reqd.
    for j in range(1,len(inp)):
      if (inp[j]<pivot):
        inp[i], inp[j] = inp[j], inp[i]
        i+=1

    # move the pivot element to the right place
    inp[i-1], inp[0] = inp[0], inp[i-1]
    
    left = inp[:i-1]
    right = inp[i:]

    # left is lower than pivot, right is greater. Now call quicksort for these two
    (left, compcount) = quicksort(left, compcount)
    (right, compcount) = quicksort(right, compcount)
    return (left+[pivot]+right, compcount)

  else:
    return (inp, compcount)

def choosePivot(inp):
  '''
  Function to choose the pivot element in a given list for QuickSort
  Could be first element, last element, or random
  '''
  #inp[0], inp[-1] = inp[-1], inp[0]
  #piv = inp[0]

  
  mid = round(len(inp)*0.5)-1

  if inp[0]<=inp[-1]<=inp[mid] or inp[mid]<=inp[-1]<=inp[0]:
    inp[0], inp[-1] = inp[-1], inp[0]
  elif inp[-1]<=inp[mid]<=inp[0] or inp[0]<=inp[mid]<=inp[-1]:
    inp[0], inp[mid] = inp[mid], inp[0]


# Main Body
f = open('1000.txt','r')
inp = [0]*1000
for i in range(len(inp)):
  inp[i] = int(f.readline())

(inp,compcount) = quicksort(inp, 0)
print(compcount)
