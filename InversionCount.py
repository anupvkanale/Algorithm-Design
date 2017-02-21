#Count Inversions
def countInv(inp, invcount):
  if len(inp)==1:
    return ( inp, invcount)
  else:
    mid = round(len(inp)*0.5)
    left = inp[:mid]
    right = inp[mid:]

    (left, invcount) = countInv(left, invcount)
    (right,invcount) = countInv(right, invcount)

    i=0
    j=0
    k=0
    while (i<len(left) and j<len(right)):
      if (left[i]<right[j]):
        inp[k] = left[i]
        i=i+1
      else:
        inp[k] = right[j]
        j=j+1
        invcount += len(right)
      k=k+1

    while i < len(left):
        inp[k] = left[i]
        i += 1; k = k+1
    
    while j < len(right):
        inp[k] = right[j]
        j += 1; k = k+1
    
    return (inp,invcount)

# Call coutnInv

#inp = [11,45,12,2,89,4,5]  
f = open('IntegerArray.txt','r')
inp = [0]*100000
for i in range(100000):
  inp[i] = int(f.readline())
  
(out, invcount) = countInv(inp, 0)
print(invcount)
